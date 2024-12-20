from flask import Flask, render_template, request, jsonify 
import logging
import os
import json
from recommendations_engine import QUESTIONS, RECOMMENDATIONS
from processing import build_network
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    try:
        # Process QUESTIONS and RECOMMENDATIONS data into a "processed_data" format
        processed_data = []
        for task, goals in RECOMMENDATIONS.items():
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
        net = build_network(RECOMMENDATIONS)
        
        # Generate the HTML representation of the network
        graph_html = net.generate_html()

        # Render the template, passing in the graph HTML and processed_data
        return render_template(
            'index.html',
            graph_body=graph_html,
            initial_data=json.dumps(processed_data)
        )
       
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
        node_id = request.json.get('node_id')
        if not node_id:
            return jsonify({"error": "No node ID provided"}), 400
        
        # Find the matching leaderboard data
        # Remember, the nodes in PyVis have IDs like "leaderboard_task_goal_lbname"
        # So we need to parse node_id or find a suitable way to match it.
        # Assuming node_id is something like "leaderboard_<task>_<goal>_<leaderboard>"
        # we can reconstruct the original leaderboard name from node_id if needed.
        
        # However, the code below attempts a direct match. If that doesn't work because of the updated IDs,
        # you might need to parse the node_id to extract leaderboard name.
        
        # Extracting leaderboard name from node_id
        # node_id format: leaderboard_<task>_<goal>_<leaderboard_name>
        # We can split by '_' and rejoin for leaderboard name if it has spaces
        # e.g., node_id = "leaderboard_chain_agents_quality_Artificial Analysis"
        
        if node_id.startswith('leaderboard_'):
            parts = node_id.split('_', 3)  # split into 4 parts: [leaderboard, task, goal, lbname...]
            if len(parts) == 4:
                # The fourth part is the leaderboard name
                lb_name = parts[3]
            else:
                return jsonify({"error": "Invalid leaderboard node ID format"}), 400

            # Now search in RECOMMENDATIONS for that leaderboard name
            for task, goals in RECOMMENDATIONS.items():
                for goal, leaderboards in goals.items():
                    for leaderboard in leaderboards:
                        if leaderboard['leaderboard'] == lb_name:
                            return jsonify({
                                'leaderboard': leaderboard['leaderboard'],
                                'tooltip': leaderboard.get('tooltip', ''),
                                'source': leaderboard['leaderboard_link']['url'],
                                'methodology': leaderboard.get('methodology', {}).get('url', ''),
                                'analysis_tips': leaderboard.get('analysis_tips', [])
                            })

        return jsonify({"error": "Leaderboard not found"}), 404
        
    except Exception as e:
        logging.error(f"Error in filter_data route: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
