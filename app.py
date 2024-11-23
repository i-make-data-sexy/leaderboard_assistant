# ========================================================================
#   Imports
# ======================================================================== 

from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
import logging
import os

# ========================================================================
#   Logging
# ======================================================================== 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# ========================================================================
#   App Config
# ======================================================================== 

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Configure secret key
app.secret_key = os.getenv('AI_LEAD_FLASK_SECRET_KEY', 'default_secret_key')  

app.config['SESSION_TYPE'] = 'filesystem'

# In-memory structure to guide the question flow
QUESTIONS = {
    "goal": {
        "question": "What do you want to evaluate?",
        "tooltip": "There are many metrics leaderboards provide. The answer to this question will help whittle down the list of metrics to choose from.",
        "options": [
            "Quality", 
            "Speed",
            "Latency", 
            "Cost", 
            "Context Window"
            ],
        "next": "task"
    },
    "task": {
        "question": "What task do you want the model to do?",
        "tooltip": "This list isn't exhaustive of what AI can do; it's more representative of the types of tasks that have associated intelligence-leaning performance metrics.",
        "options": [
            "Chat", 
            "Code", 
            "Creative writing", 
            "Analyze data", 
            "Math", 
            "Complex reasoning", 
            "Text to speech", 
            "Speech to text", 
            "Text to image", 
            "Image to text", 
            "Text to video"
            ],
        "next": "recommendation"
    },
}

# Recommendations with detailed metric information
RECOMMENDATIONS = {
    "Quality": {
        "Chat": [
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score.",
                    "You can sort the table by each column."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "metrics": [
                    {
                        "metric_name": "Overall",
                        "metric_measures": "The general ranking of the model across all task categories.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Overall w/ Style Control",
                        "metric_measures": "Ranking considering the model's ability to maintain stylistic consistency in its responses.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Hard Prompts (Overall)",
                        "metric_measures": "Model performance on challenging or complex prompts.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Hard Prompts w/ Style Control",
                        "metric_measures": "Model's ranking on hard prompts, also considering style consistency.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Instruction Following",
                        "metric_measures": "How well the model follows explicit user instructions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Coding",
                        "metric_measures": "Model's ability to understand and generate code effectively.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Math",
                        "metric_measures": "Model's accuracy in solving mathematical problems.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Multi-Turn",
                        "metric_measures": "Model's performance in multi-turn conversations, reflecting conversational consistency and coherence.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Longer Query",
                        "metric_measures": "Effectiveness in handling and responding accurately to longer, more complex queries.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "metric_name": "Arena Score",
                        "metric_measures": "Ranks based on LLM performance in head-to-head comparisons. This score is derived using the Elo rating system, a method traditionally employed in chess and other competitive games to assess the relative skill levels of players.",
                        "score_interpretation": "Score ranges from 1 – thousands (higher is better)."
                    }
                ]
            },
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models#quality"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better across all of their metrics.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
                    {
                        "metric_name": "Quality Index",
                        "metric_measures": "A composite score that evaluates the overall quality of the AI model's output across multiple tasks, balancing correctness, coherence, and relevance.",
                        "score_interpretation": "Higher scores indicate better quality."
                    },
                    {
                        "metric_name": "Reasoning & Knowledge (MMLU)",
                        "metric_measures": "Measures the model's ability to answer questions across 57 academic subjects, testing both reasoning and world knowledge.",
                        "score_interpretation": "Higher scores reflect a stronger ability to reason and recall factual information."
                    },
                    {
                        "metric_name": "Scientific Reasoning & Knowledge (GPQA Diamond)",
                        "metric_measures": "Evaluates the model's ability to answer questions requiring scientific reasoning, logical problem-solving, and subject-specific expertise.",
                        "score_interpretation": "Higher scores denote superior scientific understanding and problem-solving accuracy."
                    },
                    {
                        "metric_name": "Quantitative Reasoning (MATH)",
                        "metric_measures": "Tests the model’s mathematical reasoning and problem-solving skills, including algebra, calculus, and number theory.",
                        "score_interpretation": "Higher scores indicate better mathematical reasoning and accuracy."
                    },
                    {
                        "metric_name": "Coding (HumanEval)",
                        "metric_measures": "Evaluates the model's ability to generate syntactically correct and functional code based on problem statements.",
                        "score_interpretation": "Higher scores reflect greater coding proficiency and correctness."
                    },
                    {
                        "metric_name": "Communication (LMSys Chatbot Arena ELO Score)",
                        "metric_measures": "Measures the model’s performance in conversational settings, evaluating communication skills, coherence, and engagement based on user feedback.",
                        "score_interpretation": "Higher ELO scores represent superior conversational ability, as judged through head-to-head comparisons."
                    }
                ]
            }
        ],
        "Code": {
            "leaderboard": "CodeBench",
            "leaderboard_link": {
                "text": "Visit CodeBench Leaderboard",
                "url": "https://codebench.com"
            },
            "metrics": [
                {
                    "metric_name": "Code Quality",
                    "metric_def": "Evaluates the accuracy, readability, and efficiency of generated code.",
                    "metric_report_link": {
                        "text": "View Code Quality Report",
                        "url": "https://codebench.com/quality"
                    },
                    "learn_more_link": {
                        "text": "Learn more about Code Quality",
                        "url": "https://codebench.com/docs/quality"
                    },
                    "analysis_tips": [
                        "High-quality code generation reduces debugging effort.",
                        "Focus on models with strong support for your programming language."
                    ]
                }
            ]
        }
    },
    "Speed": {
        # Similar structure as "Quality" but with speed-specific metrics
    },
    "Latency": {
        # Similar structure as "Quality" but with latency-specific metrics
    },
    "Cost": {
        # Similar structure as "Quality" but with cost-specific metrics
    },
    "Context Window": {
        # Similar structure as "Quality" but with context window-specific metrics
    }
}




# RECOMMENDATIONS = {
#     "Quality": {
#         "Chat": 
#             {"leaderboard": "Chatbot Arena",
#              "metrics": {
#                  "metric_name": "Overall",
#                  "metric_def": "The general ranking of the model across all task categories."},},
#         "Code": "",
#         "Creative writing": "",
#         "Analyze data": "",
#         "Math": "",
#         "Complex reasoning": "",
#         "Text to speech": "",
#         "Speech to text": "",
#         "Text to image": "",
#         "Image to text": "",
#         "Text to video": "",
        
#     },
#     "Code": {
#         "Open Source": "We recommend CodeGen.",
#         "Proprietary": "We recommend OpenAI's Codex.",
#         "No Preference": "Consider both CodeGen and Codex."
#     },
#     "Write Creatively": {
#         "Open Source": "Try EleutherAI's GPT-NeoX.",
#         "Proprietary": "Use OpenAI's GPT-4 for creative writing.",
#         "No Preference": "Both GPT-NeoX and GPT-4 are excellent."
#     },
#     "Analyze Data": {
#         "Open Source": "We recommend BigScience's BLOOM.",
#         "Proprietary": "We recommend Google's PaLM.",
#         "No Preference": "Explore both BLOOM and PaLM."
#     }
# }

# Home Route
@app.route('/')
def index():
    session.clear()  # Clear previous session data
    return render_template('index.html')

# Question Route
@app.route('/question/<key>', methods=['GET', 'POST'])
def question(key):
    # Check if key exists in QUESTIONS
    if key not in QUESTIONS:
        return redirect(url_for('index'))

    question_data = QUESTIONS[key]

    # Form for the current question
    class QuestionForm(FlaskForm):
        choice = RadioField(
            question_data["question"],
            choices=[(option, option) for option in question_data["options"]],
            render_kw={"class": "form-check-input"}
        )
        submit = SubmitField('Next')

    form = QuestionForm()

    # Handle form submission
    if form.validate_on_submit():
        session[key] = form.choice.data  # Save the choice in the session
        next_key = question_data.get("next")
        if next_key == "recommendation":
            return redirect(url_for('recommendation'))
        return redirect(url_for('question', key=next_key))

    return render_template('question.html', form=form, key=key)

# Recommendation Route
@app.route('/recommendation')
def recommendation():
    task = session.get("task")
    preference = session.get("preference")
    if not task or not preference:
        return redirect(url_for('index'))

    recommendation = RECOMMENDATIONS[task][preference]
    return render_template('recommendation.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
