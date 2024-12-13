# ========================================================================
#   Imports
# ======================================================================== 

import json
from app import RECOMMENDATIONS

# ========================================================================
#   Functions
# ======================================================================== 

def print_nested_structure(data, indent=0, max_depth=2, current_depth=0):
    """Helper function to print nested dictionary structure without all details"""
    if current_depth >= max_depth:
        return "..."
    
    if isinstance(data, dict):
        output = "{\n"
        for key, value in list(data.items())[:3]:  # Limit to first 3 items
            output += " " * (indent + 2) + f'"{key}": '
            output += print_nested_structure(value, indent + 2, max_depth, current_depth + 1)
            output += ",\n"
        if len(data) > 3:
            output += " " * (indent + 2) + "...\n"
        output += " " * indent + "}"
        return output
    elif isinstance(data, list):
        if len(data) == 0:
            return "[]"
        return f"[/* {len(data)} items */]"
    else:
        return f'"{data}"' if isinstance(data, str) else str(data)

# Load and transform the data
def transform_data(recommendations):
    """Transform the recommendations data from goal->task to task->goal structure"""
    new_structure = {}
    
    # Get all tasks
    all_tasks = set()
    for goal in recommendations:
        all_tasks.update(recommendations[goal].keys())
    
    # Reorganize by task first
    for task in all_tasks:
        new_structure[task] = {}
        for goal in recommendations:
            if task in recommendations[goal]:
                new_structure[task][goal] = recommendations[goal][task]
    
    return new_structure

# Create new questions structure
NEW_QUESTIONS = {
    "task": {
        "question": "What do you want the model to do?",
        "tooltip": "This list isn't exhaustive of what AI can do; it's more representative of the types of tasks that have associated intelligence-leaning performance benchmarks.",
        "options": [
            "Chain agents",
            "Chat",
            "Solve complex problems",
            "Generate code",
            "Generate images",
            "Generate text",
            "Generate video",
            "Solve math problems",
            "Convert speech to text",
            "Convert text to speech"
        ],
        "next": "goal"
    },
    "goal": {
        "question": "What do you want to evaluate?",
        "tooltip": "There are many benchmark metrics leaderboards provide. The answer to this question will help whittle down the list of benchmarks to choose from.",
        "options": [
            "Quality",
            "Speed",
            "Latency",
            "Cost",
            "Context Window"
        ],
        "next": "recommendation"
    }
}

# Transform the data
new_recommendations = transform_data(RECOMMENDATIONS)

# Print example of new structure
print("\nNew Questions Structure:")
print(print_nested_structure(NEW_QUESTIONS))

print("\nExample of New Recommendations Structure (Chat task):")
if "Chat" in new_recommendations:
    print(print_nested_structure({"Chat": new_recommendations["Chat"]}, max_depth=3))

# Validation
def validate_transformation(original, transformed):
    """Validate that no data was lost in transformation"""
    all_original_entries = sum(len(goal_data) for goal_data in original.values())
    all_transformed_entries = sum(len(task_data) for task_data in transformed.values())
    
    print("\nValidation:")
    print(f"Original entries: {all_original_entries}")
    print(f"Transformed entries: {all_transformed_entries}")
    print("Transformation complete:", all_original_entries == all_transformed_entries)

validate_transformation(RECOMMENDATIONS, new_recommendations)

# Example of accessing specific benchmarks
example_task = "Chat"
example_goal = "Quality"
if example_task in new_recommendations and example_goal in new_recommendations[example_task]:
    print(f"\nExample benchmarks for {example_task} - {example_goal}:")
    benchmarks = new_recommendations[example_task][example_goal][0]["benchmarks"]
    for benchmark in benchmarks[:2]:  # Show first 2 benchmarks
        print(f"\n{benchmark['benchmark_name']}:")
        print(f"Measures: {benchmark['benchmark_measures']}")
        print(f"Interpretation: {benchmark['score_interpretation']}")