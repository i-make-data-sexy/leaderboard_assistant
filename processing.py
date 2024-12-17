# ========================================================================
#   Imports
# ======================================================================== 

import pandas as pd
import json
from pyvis.network import Network

# ========================================================================
#   Functions
# ======================================================================== 

def build_network(df):
    # Initialize the network with predefined size and undirected graph type
    net = Network(height='500px', width='100%', directed=False)
    
    # Define font settings once to ensure consistency
    label_font = {
        'size': 30,
        'color': '#333333',
        'face': 'Ek Mukta',
        'background': 'rgba(255, 255, 255, 0.8)'
    }
    
    # Retrieve the project name from the DataFrame (fallback to default if missing)
    project_name = 'Start Here'
    
    # Add the central "Project" node to the network
    net.add_node(
        f'project_{project_name}',                  # Unique node ID   
        label=project_name,                         # Displayed label
        title=project_name,                         # Tooltip
        color='#8bb42d',                            # Green
        size=80,                                    # Custom size   
        font=label_font                             # Custom font settings
    )
    
    # Use sets to track added nodes and avoid duplicates
    added_tasks = set()                       
    added_goals = set()                    
    added_leaderboards = set()                            
    
    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        task = row['Task']                  # Retrieve Task value
        goal = row['Goal']                  # Retrieve Goal value
        leaderboard = row['Leaderboard']    # Retrieve Leaderboard value
        
        # Add a Task node if it hasn't been added already
        if task not in added_tasks:
            net.add_node(
                f'task_{task}',             # Unique node ID for task
                label=task,                 # Displayed label
                title=task,                 # Tooltip text
                color='#0273be',            # Orange
                size=60,                    # Custom size
                font=label_font             # Custom font settings
            )
            added_tasks.add(task)           # Add task to the set
            
            # Connect the Task node to the Project node
            net.add_edge(f'project_{project_name}', f'task_{task}', color='#999999')
        
        # Add Goal node if it hasn't been added already
        if goal and goal not in added_goals:
            net.add_node(
                f'goal_{goal}',
                label=goal,
                title=goal,
                color='#ffa500',              # Orange
                size=50,
                font=label_font
            )
            added_goals.add(goal)
            
            # Link to parent task node
            net.add_edge(f'task_{task}', f'goal_{goal}', color='#999999')
        
        # Add T@sk node with explicitly empty label and font settings
        if leaderboard and leaderboard not in added_leaderboards:
            net.add_node(
                f'leaderboard_{leaderboard}',
            label='',                                   # Empty string for label
                title=leaderboard,                      # Keep tooltip
                color='#b8c1c7',                        # Made lighter to add contrast to outline   
                size=40,
                font=label_font
            )
            # Add edge to parent goal or task
            added_leaderboards.add(leaderboard)
            
            # Determine parent node ID based on presence of goal
            parent_id = f'goal_{goal}' if goal else f'task_{task}'
            
            # Link to parent node
            net.add_edge(parent_id, f'leaderboard_{leaderboard}', color='#999999')

    # Network options
    options = {
        'layout': {
            'hierarchical': {
                'enabled': True,                        # Enable hierarchical layout
                'levelSeparation': 200,                 # Vertical spacing between levels
                'nodeSpacing': 150,                     # Horizontal spacing between nodes
                'treeSpacing': 200,                     # Spacing between trees
                'direction': 'UD',                      # Top to bottom direction
                'sortMethod': 'directed'                # Sort based on edge direction
            }
        },
        'nodes': {
            'font': label_font,                         # Apply font settings to all nodes
            'shape': 'dot',                             # Circular node shape
            'borderWidth': 2,                           # Border width
            'borderWidthSelected': 4                    # Border width when selected
        },
        'edges': {
            'smooth': False,                            # Disable edge smoothing
            'width': 1,                                 # Edge width
            'color': '#999999'                          # Default edge color
        },
        'physics': {
            'enabled': False                            # Disable physics-based layout
        },
        'interaction': {
            'hover': True                               # Enable hover interactions for tooltips
        }
    }
    
    # Apply options to the network
    net.set_options(json.dumps(options))
    
    # Return the network
    return net