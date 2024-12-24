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
        
        # Add this right after reloading
        with open('recommendations_engine.py', 'r') as f:
            content = f.read()
        
        # Process QUESTIONS and RECOMMENDATIONS data into a "processed_data" format
        # Get query parameters for filtering tasks and goals
        tasks_selected = request.args.getlist('tasks')   # Retrieves tasks from query params like ?tasks=chat&tasks=generate_text
        goals_selected = request.args.getlist('goals')   # Retrieves goals from query params like ?goals=quality&goals=speed

        all_tasks = list(RECOMMENDATIONS.keys())
        
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
                    
        # If only tasks are selected, filter only by tasks
        elif tasks_selected:
            filtered_recs = {task: goals for task, goals in RECOMMENDATIONS.items() if task in tasks_selected}
            # ADD LOGGING: Show filtered_recs for tasks only
            
        # If only goals are selected, filter only by goals
        elif goals_selected:
            filtered_recs = {}
            for task, goals in RECOMMENDATIONS.items():
                filtered_goals = {goal: leaderboards for goal, leaderboards in goals.items() if goal in goals_selected}
                if filtered_goals:
                    filtered_recs[task] = filtered_goals
            
        else:
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
        # Force reload recommendations module
        import recommendations_engine
        importlib.reload(recommendations_engine)
        global RECOMMENDATIONS
        RECOMMENDATIONS = recommendations_engine.RECOMMENDATIONS

        node_id = request.json.get('node_id')
        if not node_id:
            return jsonify({"error": "No node ID provided"}), 400

        if node_id.startswith('leaderboard_'):
            # Example: nodeId is "leaderboard_Generate text_Speed_KLU"
            parts = node_id.split('_', 3)  
            if len(parts) < 4:
                return jsonify({"error": "Invalid leaderboard node ID format"}), 400

            task = parts[1]
            goal = parts[2]
            lb_name = parts[3]
            
            # Only look in the specific task and goal section
            if task in RECOMMENDATIONS and goal in RECOMMENDATIONS[task]:
                leaderboards = RECOMMENDATIONS[task][goal]
                
                # Look for our leaderboard only in this section
                for lb in leaderboards:
                    if lb['leaderboard'] == lb_name:
                        bench_obj = {}
                        if 'benchmarks' in lb:
                            for bench in lb['benchmarks']:
                                name = bench.get('benchmark_name', 'Untitled Benchmark')
                                bench_obj[name] = {
                                    'measures': bench.get('benchmark_measures', ''),
                                    'score_interpretation': bench.get('score_interpretation', '')
                                }
                        
                        return jsonify({
                            'leaderboard': lb['leaderboard'],
                            'tooltip': lb.get('tooltip', ''),
                            'analysis_tips': lb.get('analysis_tips', []),
                            'benchmarks': bench_obj,
                            'leaderboard_link': lb['leaderboard_link']['url'],
                            'methodology_url': lb.get('methodology', {}).get('url', ''),
                        })

        return jsonify({"error": "Leaderboard not found"}), 404
    
    except Exception as e:
        logging.error(f"Error in filter_data route: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
