# ========================================================================
#   Imports
# ======================================================================== 

from flask import Flask, render_template, request, jsonify, send_from_directory, make_response
import logging
import os
import json
import importlib
from recommendations_engine import QUESTIONS, RECOMMENDATIONS
from processing import build_network
import pandas as pd
from bs4 import BeautifulSoup


# ========================================================================
#   Configure Logging
# ========================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# ========================================================================
#   Disable Caching
# ======================================================================== 

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Disable caching for development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  

# Add this too for good measure
app.config['TEMPLATES_AUTO_RELOAD'] = True    


@app.context_processor
def utility_processor():
    def get_version():
        return str(os.path.getmtime('recommendations_engine.py'))
    return dict(version=get_version)


# ========================================================================
#   Routes
# ======================================================================== 

@app.route('/')
def index():
    try:
        # Force reload the recommendations module
        import recommendations_engine
        importlib.reload(recommendations_engine)
        
        # Process QUESTIONS and RECOMMENDATIONS data into a "processed_data" format
        # Get query parameters for filtering tasks and goals
        tasks_selected = request.args.getlist('tasks')   # Retrieves tasks from query params like ?tasks=chat&tasks=generate_text
        goals_selected = request.args.getlist('goals')   # Retrieves goals from query params like ?goals=quality&goals=speed
        
        # ADD LOGGING: Print selected tasks and goals
        logging.info(f"Tasks selected: {tasks_selected}")
        logging.info(f"Goals selected: {goals_selected}")

        # ADD LOGGING: Print all available tasks and goals from RECOMMENDATIONS
        # This helps confirm that the keys you selected actually exist
        all_tasks = list(RECOMMENDATIONS.keys())
        # logging.info(f"All available tasks in RECOMMENDATIONS: {all_tasks}")
        # # If needed, you can also log goals for each task
        # for t, g_dict in RECOMMENDATIONS.items():
        #     logging.info(f"Task: {t}, available goals: {list(g_dict.keys())}")
        
        # Add these lines right after you get RECOMMENDATIONS and before filtering logic:
        # NEW: Logging to see what keys RECOMMENDATIONS has.
        logging.info(f"Tasks available in RECOMMENDATIONS: {list(RECOMMENDATIONS.keys())}")
        for t, g_dict in RECOMMENDATIONS.items():
            logging.info(f"For task '{t}', goals available: {list(g_dict.keys())}")


        
        # If tasks and goals are specified, filter RECOMMENDATIONS
        if tasks_selected and goals_selected:              
            filtered_recs = {}
            for task, goals in RECOMMENDATIONS.items():
                if task not in tasks_selected:
                    continue
                filtered_goals = {}
                for goal, leaderboards in goals.items():
                    if goal not in goals_selected:
                        continue
                    filtered_goals[goal] = leaderboards
                if filtered_goals:
                    filtered_recs[task] = filtered_goals
            
            # ADD LOGGING: Show what's in filtered_recs when both tasks and goals are filtered
            logging.info(f"Filtered recommendations (tasks & goals): {json.dumps(filtered_recs, indent=2)}")        
                    
        # If only tasks are selected, filter only by tasks
        elif tasks_selected:
            logging.info("Filtering by tasks only")
            filtered_recs = {task: goals for task, goals in RECOMMENDATIONS.items() if task in tasks_selected}
            # ADD LOGGING: Show filtered_recs for tasks only
            logging.info(f"Filtered recommendations (tasks only): {json.dumps(filtered_recs, indent=2)}")
            
        # If only goals are selected, filter only by goals
        elif goals_selected:
            logging.info("Filtering by goals only")
            filtered_recs = {}
            for task, goals in RECOMMENDATIONS.items():
                filtered_goals = {goal: leaderboards for goal, leaderboards in goals.items() if goal in goals_selected}
                if filtered_goals:
                    filtered_recs[task] = filtered_goals
            # ADD LOGGING: Show filtered_recs for goals only
            logging.info(f"Filtered recommendations (goals only): {json.dumps(filtered_recs, indent=2)}")
            
        else:
            logging.info("No filters selected, using original RECOMMENDATIONS")
            filtered_recs = RECOMMENDATIONS
            
        processed_data = []
        for task, goals in filtered_recs.items():
            for goal, leaderboards in goals.items():
                for leaderboard_info in leaderboards:
                    for benchmark in leaderboard_info.get('benchmarks', []):
                        row = {
                            'Task': task,
                            'Goal': goal,
                            'Leaderboard': leaderboard_info['leaderboard'],
                            'Tips': "\n".join(leaderboard_info.get('analysis_tips', [])),
                            'Source': leaderboard_info['leaderboard_link']['url'],
                            'Tooltip': leaderboard_info.get('tooltip', ''),
                            'Methodology': leaderboard_info.get('methodology', {}).get('url', '')
                        }
                        processed_data.append(row)
        
        # ADD LOGGING: Confirm how many tasks and goals ended up in filtered_recs before building network
        logging.info(f"Final filtered_recs structure before build_network: {json.dumps(filtered_recs, indent=2)}")

        # Build the PyVis network
        net = build_network(filtered_recs)
        
        # If net is None or empty, that might indicate an empty filtered_recs
        if net is None:
            logging.warning("Network returned by build_network is None. filtered_recs might be empty.")
        
        #  Get network data for vis.js
        network_data = {
            'nodes': net.nodes,
            'edges': net.edges
        }

        # Render the template, passing in the most recent graph HTML and processed_data
        response = render_template(
            'index.html',
            network_data=json.dumps(network_data),
            initial_data=json.dumps(processed_data),
            recommendations_data=RECOMMENDATIONS
        )
        
        # Create a response object that I can modify with headers
        # Add cache-control headers to prevent browser caching
        # 'no-cache': browser must revalidate with server before using cached version
        # 'no-store': browser shouldn't store the response at all
        # 'must-revalidate': browser must check if the content has changed
        response = make_response(response)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        
        # 'Pragma: no-cache' for backwards compatibility with HTTP/1.0
        response.headers['Pragma'] = 'no-cache'
        
        # Set expiration to 0 to help prevent caching in older browsers
        response.headers['Expires'] = '0'
        
        # Return the modified response with no-cache headers
        return response

        
       
    except Exception as e:
        logging.error(f"Error in index route: {str(e)}")
        return render_template(
            'index.html',
            error=str(e),
            graph_body='',   # If we have an error, just pass an empty graph_body
            initial_data='[]'
        )

@app.route('/filter_data', methods=['POST'])
def filter_data():
    try:
        # Trying to resolve caching issue
        import recommendations_engine
        importlib.reload(recommendations_engine)
        # Re-import after reload
        from recommendations_engine import RECOMMENDATIONS  
        
        # Add logging to see what's being loaded
        logging.info("Reloaded RECOMMENDATIONS module")
        
        node_id = request.json.get('node_id')
        if not node_id:
            return jsonify({"error": "No node ID provided"}), 400

        if node_id.startswith('leaderboard_'):
            # Example: nodeId is "leaderboard_Chat_Quality_Vellum LLM Leaderboard"
            # We'll parse the nodeId but let's keep it simple:
            parts = node_id.split('_', 3)  # e.g. ['leaderboard', 'Chat', 'Quality', 'Vellum LLM Leaderboard']
            if len(parts) < 4:
                return jsonify({"error": "Invalid leaderboard node ID format"}), 400

            lb_name = parts[3]  # "Vellum LLM Leaderboard"
            
            # Now search in RECOMMENDATIONS for that matching leaderboard name
            for task, goals in RECOMMENDATIONS.items():
                for goal, leaderboards in goals.items():
                    for lb in leaderboards:
                        if lb['leaderboard'] == lb_name:
                            # Found the correct leaderboard object
                            
                            # Convert the 'benchmarks' list into an object
                            # so React can do: Object.entries(data.benchmarks)
                            bench_obj = {}
                            if 'benchmarks' in lb:
                                for bench in lb['benchmarks']:
                                    name = bench.get('benchmark_name', 'Untitled Benchmark')
                                    bench_obj[name] = {
                                        'measures': bench.get('benchmark_measures', ''),
                                        'score_interpretation': bench.get('score_interpretation', '')
                                    }
                            
                            # Logging to diagnose caching issue
                            logging.info(f"Sending benchmark data for {lb_name}: {json.dumps(bench_obj, indent=2)}")
                            
                            # Build final response
                            return jsonify({
                                'leaderboard': lb['leaderboard'],  # Full name
                                'tooltip': lb.get('tooltip', ''),
                                'analysis_tips': lb.get('analysis_tips', []),
                                'benchmarks': bench_obj,
                                'leaderboard_link': lb['leaderboard_link']['url'],
                                # If you need text too, you can do: lb['leaderboard_link']['text']
                                
                                # The 'methodology' may be nested, so handle carefully
                                'methodology_url': lb.get('methodology', {}).get('url', ''),
                                # or if you want to call it 'methodology', do:
                                # 'methodology': lb.get('methodology', {}).get('url', '')
                            })

        # Add this right before your return jsonify line
        logging.info(f"Sending benchmark data for {lb_name}: {json.dumps(bench_obj, indent=2)}")
        
        return jsonify({"error": "Leaderboard not found"}), 404
    
    except Exception as e:
        logging.error(f"Error in filter_data route: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
