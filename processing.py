# ========================================================================
#   Imports
# ======================================================================== 

import json
from pyvis.network import Network


# ========================================================================
#   Build Default Network Graph Structure
# ======================================================================== 

def build_network(recommendations):
    # print(f"Building network with recommendations: {len(recommendations)} tasks")
    if not recommendations:
        print("Warning: Empty recommendations provided")
        return None  # or handle appropriately

    # Adjust height of network graph here
    net = Network(directed=False)

    # Define a common font style
    label_font = {
        'size': 30,
        'color': '#333333',
        'face': 'Ek Mukta',
        'background': 'rgba(255, 255, 255, 0.8)'
    }

    # Add the "Start here" node
    net.add_node(
        'start',
        label='Start here',
        # title='Start here',
        color='#E90555',
        size=70,
        font=label_font
    )

    # Keep track of what we've added to avoid duplicates
    added_tasks = set()
    added_goals = set()
    added_leaderboards = set()

    # Build the network from the dictionary
    for task, goals_dict in recommendations.items():
        # Add task node
        if task not in added_tasks:
            net.add_node(
                f'task_{task}',
                label=task,
                title=f"Task: {task}",
                color='#ffa500',                                       # Orange
                size=60,
                font=label_font
            )
            added_tasks.add(task)
            net.add_edge('start', f'task_{task}', color='#999')

        # Add goals under each task
        for goal, leaderboards in goals_dict.items():
            goal_id = f'goal_{task}_{goal}'
            if goal_id not in added_goals:
                net.add_node(
                    goal_id,
                    label=goal,
                    title=f"Benchmark to compare: {goal}",
                    color='#0273be',                                    # Blue
                    size=50,
                    font=label_font
                )
                added_goals.add(goal_id)
                net.add_edge(f'task_{task}', goal_id, color='#999')

            # Add leaderboards under each goal
            for lb_data in leaderboards:
                lb_name = lb_data["leaderboard"]                        # Full name
                lb_label = lb_data.get("leaderboard_abbrev", lb_name)   # Label

                # Construct the custom title (tooltip) string
                lb_title = (
                    f"Leaderboard: {lb_name}\n\n"
                    f"Overview: {lb_data.get('tooltip', '')}\n\n"
                    f"Learn more: Select the node (dot) to learn more about this leaderboard."
                )

                lb_id = f'leaderboard_{task}_{goal}_{lb_name}'
                if lb_id not in added_leaderboards:
                    net.add_node(
                        lb_id,
                        label=lb_label,
                        title=lb_title,                                 # The two-line format
                        color='#8bb42d',
                        size=40,

                        # data: store the entire dictionary if you need it for your modal
                        data={
                            'type': 'leaderboard',
                            'leaderboard_info': lb_data
                        },

                        font={
                            'size': 20,
                            'color': '#333',
                            'face': 'Ek Mukta',
                            'background': 'rgba(255, 255, 255, 0.8)'
                        }
                    )
                    added_leaderboards.add(lb_id)
                    net.add_edge(goal_id, lb_id, color='#999')

                # Add benchmark nodes
                benchmarks = lb_data.get('benchmarks', [])
                for benchmark in benchmarks:
                    
                    # NEW: Extract the benchmark name to use as label
                    benchmark_name = benchmark.get('benchmark_name', 'Unknown Benchmark')  # Using get() to avoid errors if key doesn't exist
                    
                    # NEW: Extract measures for the tooltip/title
                    benchmark_measures = benchmark.get('benchmark_measures', '')

                    # NEW: Adjusting the benchmark_id to include benchmark_name
                    # Replace spaces in benchmark_name with underscores to avoid ID issues
                    benchmark_id = f"benchmark_{task}_{goal}_{lb_name}_{benchmark_name.replace(' ', '_')}"
                    
                    benchmark_title = (
                                        f"Benchmark: {benchmark_name}\n\n"
                                        f"Measures: {benchmark_measures}"
                                      )

                    # NEW: Use benchmark_name for label, benchmark_measures for title
                    net.add_node(
                        benchmark_id,
                        label=benchmark_name,               
                        title=benchmark_title,                          # Formatted title (tooltip)
                        color='#999999',
                        size=30,
                        font={
                            'size': 18,
                            'color': '#333',
                            'face': 'Ek Mukta',
                            'background': 'rgba(255, 255, 255, 0.8)'
                        }
                    )
                    net.add_edge(lb_id, benchmark_id, color='#999999')

    return net
