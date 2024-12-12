# ========================================================================
#   Prompt info
# ======================================================================== 

# Claude Chat
# https://claude.ai/chat/f81e0f63-f70a-472b-8956-e7c44cb01c54

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
            "Generate video"
            "Solve math problems", 
            "Convert speech to text", 
            "Convert text to speech" 
            ],
        "next": "goal"
    },
    "goal": {
        "question": "What do you want to evaluate?",
        "tooltip": "There are many metrics leaderboards provide. The answer to this question will help whittle down the list of benchmarks to choose from.",
        "options": [
            "Quality", 
            "Speed",
            "Latency", 
            "Cost", 
            "Context Window"
            ],
        "next": "recommendation"
    },
    
}

# Recommendations with detailed benchmark information
RECOMMENDATIONS = {
    # Evaluate: Quality
    "Quality": {
        "Chain agents": [
            {
                # VERIFIED
                "leaderboard": "SEAL",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://scale.com/leaderboard/tool_use"
                },
                "tooltip": "They break up ToolComp into two subsets: ToolComp-Enterprise, which tests usage of 11 tools, and ToolComp-Chat, which tests usage of 2 common chatbot tools (Python Interpreter and Google Search).",
                "analysis_tips": [
                    "Their introduction includes a handy table that compares the tasks included in their benchmark (ToolComp) to other benchmarks.",
                    "In their Data Sample section they include example tasks each model was evaluated on, e.g., 'Calculate the average daytime temperature in Paris during the week of Halloween (October 29th to November 4th, 2023).' They provide 5 examples you can toggle through.",
                    "If you want to gain a better understanding of how agents work under the hood, I highly recommend reading the pseudo-code the models generate. Search for 'thought:' in the Data Sample section.",
                    "In the Prompt Creation section, they categorize the prompts. This is really useful because if your app is going to be used in a vertical not as well represented (e.g., Architecture or Geology), you may want to discount the usefulness of this leaderboard.",
                    ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://scale.com/leaderboard/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Score",
                        "benchmark_measures": "Score calculates the mean of ToolComp-Enterprise and ToolComp-Chat. ToolComp-Enterprise assesses models on tasks requiring the use of 11 distinct tools, reflecting complex scenarios typical in enterprise settings. ToolComp-Chat evaluates models on tasks involving two common tools—Google Search and Python Interpreter—focusing on general-purpose chatbot capabilities.",
                        "score_interpretation": "Score ranges from 1 to 100 (higher is better).",
                    }
                ]
            }
        ],
        "Chat": [
                        {
                # VERIFIED
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models#quality"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                # TIPS FOR ARTIFICIAL ANALYSIS
                "analysis_tips": [
                    "Higher is better across all of their metrics.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.", 
                    "Under their 'Quality Evaluations' section, they only show 15 of the available 81 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Communication (LMSys Chatbot Arena ELO Score)",
                        "benchmark_measures": "Measures the model's performance in conversational settings, evaluating communication skills, coherence, and engagement based on user feedback.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate superior conversational ability, as judged by one-to-one comparisons."
                    }
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score. (The 'Sort by Arena Score is a gray button above the table.)",
                    "You can sort the table by each column.",
                    "The Full Leaderboard tab includes columns for Organization and License [type]. This is handy for identifying models that are proprietary, non-commercial, MIT, etc.",
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and the nature of the prompt source (e.g., configurable, fixed, or crowd).",
                    "I included Arena Score, which utilizes the Elo rating system, a method traditionally employed in chess and other competitive games to assess the relative skill levels of players. but it may not effectively capture how well a model handles domain-specific tasks or real-world chatbot use cases.",
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Instruction Following",
                        "benchmark_measures": "How well the model follows explicit user instructions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Multi-Turn",
                        "benchmark_measures": "Model's performance in multi-turn conversations, reflecting conversational consistency and coherence.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Longer Query",
                        "benchmark_measures": "Effectiveness in handling and responding accurately to longer, more complex queries.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Arena Score",
                        "benchmark_measures": "Ranks based on LLM performance in head-to-head comparisons. This score is derived using the Elo rating system, a method traditionally employed in chess and other competitive games to assess the relative skill levels of players.",
                        "score_interpretation": "Score ranges from 1 – thousands (higher is better)."
                    },
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Hugging Face",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard only includes open models, so you won't find performance metrics for proprietary models here (e.g., OpenAI, Google, Anthropic, etc).",
                "analysis_tips": [
                    "You have more viewing options if you select 'table option' above the table.",
                    "I recommend filtering by just chat models. You can do this by selecting the Advanced Filters button in the search field and selecting 'Chat' from Model Type. You have other filter options as well, like model size (measured in parameters), as well as flags.",
                    "If you're building a chatbot for a more technical domain, such as medicine, law, engineering, or math, I'd also look at the MMLU-PRO benchmark.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "IFEval",
                        "benchmark_measures": "Tests model's ability to follow explicit formatting instructions.",
                        "score_interpretation": "Higher scores indicate better adherence to instructions."
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores reflect better ability to perform chained reasoning."
                    },
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Reasoning",
                        "benchmark_measures": "Vellum's label for the HellaSwag Benchmark. Assesses the model's commonsense reasoning and ability to predict plausible next steps in a scenario.",
                        "score_interpretation": "Higher scores denote better commonsense reasoning capabilities."
                    },
                ]
            }
        ],
        "Solve complex problems": [
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score. (The 'Sort by Arena Score is a gray button above the table.)",
                    "You can sort the table by each column.",
                    "The Full Leaderboard tab includes columns for Organization and License [type]. This is handy for identifying models that are proprietary, non-commercial, MIT, etc.",
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and the nature of the prompt source (e.g., configurable, fixed, or crowd).",
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/)."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Hard Prompts (Overall)",
                        "benchmark_measures": "Evaluates performance on complex, multi-step reasoning challenges.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    },
                    {
                        "benchmark_name": "Multi-Turn Reasoning",
                        "benchmark_measures": "Tests ability to maintain logical consistency across extended reasoning chains.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    },
                    {
                        "benchmark_name": "Complex Problem Solving",
                        "benchmark_measures": "Assesses ability to solve problems requiring multiple steps and consideration of various factors.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard includes several benchmarks specifically designed to test complex reasoning capabilities.",
                "analysis_tips": [
                    "This leaderboard only includes open models, so you won't find proprietary models here.",
                    "Consider both raw and processed scores for reasoning benchmarks.",
                    "Pay attention to performance on multi-step reasoning tasks.",
                    "Look for models that excel at both structured and open-ended reasoning."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "BBH (BIG-bench Hard)",
                        "benchmark_measures": "Evaluates performance on challenging prompts requiring complex reasoning.",
                        "score_interpretation": "Higher scores indicate better complex reasoning capabilities.",
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores indicate better sequential reasoning ability.",
                    },
                ]
            },
        ],
        "Generate code": [
            {
                "leaderboard": "BigCodeBench Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://bigcode-bench.github.io/"
                },
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2406.15877"
                },
                "analysis_tips": [
                    "Use Calibrated Pass@1 when evaluating models for practical scenarios where minor code fixes are acceptable.",
                    "Compare raw Pass@1 with Calibrated Pass@1 to assess the model's strict correctness versus its usability.",
                    "Pass@k metrics are helpful when determining how often models produce at least one correct solution in multiple attempts.",
                    "Calibrated Pass@1 adjusts the raw Pass@1 metric to account for common errors or omissions that might not necessarily indicate the model's inability to solve the task. It is designed to provide a fairer comparison by considering the model's intent and coding capabilities, even when the output is incomplete or imperfect.", 
                    "I find it helpful to think of Calibrated Pass@1 in terms of human developers. When developers write code, we may miss certain details like importing a library, defining helper functions, or adding boilerplate code. These omissions don't necessarily reflect poor coding skills but might stem from assumptions about the environment or the context. Similarly, LLMs sometimes generate code that is functionally correct but incomplete, such as forgetting imports or minor details that can easily be inferred.",
                    "Click 'base' or 'instructed' to remove them from the chart. This feature can be buggy. If all the models disappear, click 'Instruct' or 'Average' and return to 'Complete'.",
                    "Hard vs Full: The 'Hard' option evaluates models on more challenging or complex datasets, while 'Full' includes all datasets, providing a broader overview of model performance.",
                    "Complete, Instruct, Average: These toggles control the evaluation focus. 'Complete' assesses the model's ability to handle complete tasks, 'Instruct' focuses on instruction-following capabilities, and 'Average' represents an aggregate score across both types.",
                    "Show Models with Unknown Sizes: Enables or disables the inclusion of models whose parameter sizes or details are not disclosed. Useful for filtering out incomplete data.",
                    "Base vs Instructed: The color coding distinguishes between 'base' models (green) and 'instructed' models (gray), highlighting whether the model has undergone fine-tuning or instruction-based training."
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Calibrated Pass@1",
                        "benchmark_measures": "Adjusts the raw Pass@1 metric by accounting for common omissions or minor errors in code, such as missing imports or boilerplate. It measures the likelihood of a model generating code that solves a task correctly with slight, acceptable deviations.",
                        "score_interpretation": "Higher scores indicate better performance, emphasizing usability and real-world applicability over strict correctness.",
                    },
                    {
                        "benchmark_name": "Pass@1 (Raw)",
                        "benchmark_measures": "The percentage of tasks solved correctly by the first attempt, without calibration for omissions or partial correctness.",
                        "score_interpretation": "Higher scores indicate stricter correctness with no allowance for omissions.",
                    },
                    {
                        "benchmark_name": "Pass@k (k=5, 10)",
                        "benchmark_measures": "The percentage of tasks for which at least one of the top-k generated solutions is correct.",
                        "score_interpretation": "Higher scores indicate better overall task-solving ability across multiple attempts.",
                    }
                ]
            },
            {
                "leaderboard": "CodeXGLUE Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://microsoft.github.io/CodeXGLUE/"
                },
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2102.04664"
                },
                "tooltip": "CodeXGLUE is a benchmark suite for code intelligence developed by Microsoft Research. It includes multiple tasks focused on code understanding and generation across various programming languages.",
                "analysis_tips": [
                    "The leaderboard is divided into different tasks. Check which specific task is most relevant to your needs.",
                    "Pay attention to the programming languages covered in each task.",
                    "Consider both accuracy and efficiency metrics when comparing models.",
                    "Note that some tasks focus on code understanding while others test code generation."
                ],
                "benchmarks": [
                        {
                            "benchmark_name": "Overall",
                            "benchmark_measures": "Aggregates performance across all CodeXGLUE tasks to evaluate general code intelligence capabilities",
                            "score_interpretation": "Higher scores indicate better overall performance across all benchmarks",
                        },
                        {
                            "benchmark_name": "Clone Detection (Code-Code)",
                            "benchmark_measures": "Identifies semantically equivalent code snippets despite syntactic differences",
                            "score_interpretation": "Higher F1 scores indicate better clone detection accuracy",
                        },
                        {
                            "benchmark_name": "Defect Detection (Code-Code)",
                            "benchmark_measures": "Evaluates ability to identify bugs and potential defects in code",
                            "score_interpretation": "Higher accuracy indicates better defect detection",
                        },
                        {
                            "benchmark_name": "Cloze Test (Code-Code)",
                            "benchmark_measures": "Tests understanding of code context by predicting masked tokens in code sequences",
                            "score_interpretation": "Higher accuracy scores indicate better token prediction ability",
                        },
                        {
                            "benchmark_name": "Code Completion (Code-Code)",
                            "benchmark_measures": "Measures ability to autocomplete partial code snippets with contextually appropriate suggestions",
                            "score_interpretation": "Higher accuracy and BLEU scores indicate better completion quality",
                        },
                        {
                            "benchmark_name": "Code Refinement (Code-Code)",
                            "benchmark_measures": "Evaluates capacity to improve code quality through bug fixes and optimizations",
                            "score_interpretation": "Higher accuracy and lower error rates indicate better refinement capabilities",
                        },
                        {
                            "benchmark_name": "Code Translation (Code-Code)",
                            "benchmark_measures": "Tests ability to convert code between different programming languages while preserving functionality",
                            "score_interpretation": "Higher functional equivalence scores indicate better translation accuracy",
                        },
                        {
                            "benchmark_name": "Type Prediction (Code-Code)",
                            "benchmark_measures": "Predicts variable and function types in dynamically typed languages",
                            "score_interpretation": "Higher accuracy indicates better type inference capabilities",
                        },
                        {
                            "benchmark_name": "Natural Language Code Search (Text-Code)",
                            "benchmark_measures": "Evaluates effectiveness in finding relevant code snippets based on natural language queries",
                            "score_interpretation": "Higher MRR and NDCG scores indicate better search accuracy",
                        },
                        {
                            "benchmark_name": "Code Generation (Text-Code)",
                            "benchmark_measures": "Evaluates ability to create executable code from natural language descriptions",
                            "score_interpretation": "Higher BLEU and exact match scores indicate better generation accuracy",
                        },
                        {
                            "benchmark_name": "Code Summarization (Code-Text)",
                            "benchmark_measures": "Tests capacity to generate concise natural language descriptions of code functionality",
                            "score_interpretation": "Higher BLEU and ROUGE scores indicate better summarization quality",
                        },
                        {
                            "benchmark_name": "Documentation Translation (Text-Text)",
                            "benchmark_measures": "Measures accuracy in translating technical documentation between different human languages",
                            "score_interpretation": "Higher BLEU scores indicate better translation quality",
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
                    "The only chart relevant to coding in their 'Quality Evaluations' section is 'Coding (HumanEval)' (at the time of writing).",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.", 
                    "Under their 'Quality Evaluations' section, they only show 15 of the available 81 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Coding (HumanEval)",
                        "benchmark_measures": "Evaluates the model's ability to generate syntactically correct and functional code based on problem statements.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate greater coding proficiency and correctness.",
                    },
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score. (The 'Sort by Arena Score is a gray button above the table.)",
                    "You can sort the table by each column.",
                    "The Full Leaderboard tab includes columns for Organization and License [type]. This is handy for identifying models that are proprietary, non-commercial, MIT, etc.",
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and the nature of the prompt source (e.g., configurable, fixed, or crowd).",
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/)."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Coding",
                        "benchmark_measures": "Model's ability to understand and generate code effectively.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    }
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "analysis_tips": [
                    "The Vellum leaderboard only has one chart for coding, 'Best in Coding (HumanEval)' with a meager five models (at the time of writing), but the Model Comparison table includes a benchmark called 'Python coding', which is their alias for HumanEval.",
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page.",
                    "I really like that this leaderboard includes cutoff dates. Most do not.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Python coding",
                        "benchmark_measures": "Vellum's label for the HumanEval Benchmark. Evaluates the model's ability to generate correct Python code from problem statements.",
                        "score_interpretation": "Higher scores reflect greater proficiency in coding tasks.",
                    }
                ]
            },
        ],
        "Generate images": [
            ],
        "Generate text": [
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score. (The 'Sort by Arena Score is a gray button above the table.)",
                    "You can sort the table by each column.",
                    "The Full Leaderboard tab includes columns for Organization and License [type]. This is handy for identifying models that are proprietary, non-commercial, MIT, etc.",
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and the nature of the prompt source (e.g., configurable, fixed, or crowd).",
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/)."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Overall w/ Style Control",
                        "benchmark_measures": "Evaluates the model's ability to maintain consistent creative style and tone across responses.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    },
                    {
                        "benchmark_name": "Longer Query",
                        "benchmark_measures": "Tests ability to maintain creative coherence and style in longer compositions.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    }
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models#quality"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                # TIPS FOR ARTIFICIAL ANALYSIS
                "analysis_tips": [
                    "Higher is better across all of their metrics.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.", 
                    "Under their 'Quality Evaluations' section, they only show 15 of the available 81 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quality Index",
                        "benchmark_measures": "Evaluates overall writing quality, including creativity, coherence, and engagement.",
                        "score_interpretation": "Higher scores indicate better overall writing quality.",
                    },
                    {
                        "benchmark_name": "Communication",
                        "benchmark_measures": "Assesses effectiveness in conveying ideas and maintaining audience engagement.",
                        "score_interpretation": "Higher scores indicate better communication ability.",
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard includes metrics relevant to creative text generation and writing quality.",
                "analysis_tips": [
                    "This leaderboard only includes open models, so you won't find metrics for proprietary models.",
                    "Focus on the writing-related metrics when evaluating creative capabilities.",
                    "Consider how models perform on long-form content and coherence tests."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "TruthfulQA - Writing",
                        "benchmark_measures": "Evaluates ability to generate accurate and engaging narrative content.",
                        "score_interpretation": "Higher scores indicate better writing accuracy and quality.",
                    }
                ]
            },
            # Add to the Creative Writing array:
            {
                # VERIFIED
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Writing Style",
                        "benchmark_measures": "Evaluates the model's ability to maintain consistent tone and style in creative writing tasks.",
                        "score_interpretation": "Higher scores indicate better stylistic control and consistency.",
                    },
                    {
                        "benchmark_name": "Narrative Coherence",
                        "benchmark_measures": "Assesses the model's ability to maintain logical story flow and character consistency.",
                        "score_interpretation": "Higher scores denote better narrative structure and coherence.",
                    },
                    {
                        "benchmark_name": "Creative Adaptation",
                        "benchmark_measures": "Tests ability to creatively adapt content for different audiences and purposes.",
                        "score_interpretation": "Higher scores indicate better creative flexibility and audience awareness.",
                    }
                ]
            }    
        ], # End of Creative Writing array
        "Generate video": [],      
        "Solve math problems": [
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard is dedicated to evaluating AI through human preference. It was developed by researchers at UC Berkeley SkyLab and LMSYS. With more than 1,000,000 user votes, the platform ranks best LLM and AI chatbots using the Bradley-Terry model to generate live leaderboards.",
                "analysis_tips": [
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score. (The 'Sort by Arena Score is a gray button above the table.)",
                    "You can sort the table by each column.",
                    "The Full Leaderboard tab includes columns for Organization and License [type]. This is handy for identifying models that are proprietary, non-commercial, MIT, etc.",
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and the nature of the prompt source (e.g., configurable, fixed, or crowd).",
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/)."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Math",
                        "benchmark_measures": "Evaluates the model's accuracy in solving mathematical problems.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better.",
                    },
                ]
            },
            {
                # VERIFIED
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models#quality"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                # TIPS FOR ARTIFICIAL ANALYSIS
                "analysis_tips": [
                    "Higher is better across all of their metrics.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.", 
                    "Under their 'Quality Evaluations' section, they only show 15 of the available 81 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quantitative Reasoning (MATH)",
                        "benchmark_measures": "Tests mathematical reasoning and problem-solving skills across various domains.",
                        "score_interpretation": "Higher scores indicate better mathematical reasoning capabilities.",
                    },
                    {
                        "benchmark_name": "Scientific Reasoning & Knowledge (GPQA Diamond)",
                        "benchmark_measures": "Evaluates ability to solve quantitative problems in scientific contexts.",
                        "score_interpretation": "Higher scores indicate better scientific problem-solving ability.",
                    },
                    {
                        "benchmark_name": "Multilingual Maths (MGSM)",
                        "benchmark_measures": "Evaluates mathematical problem-solving across different languages and cultural contexts.",
                        "score_interpretation": "Higher scores indicate better multilingual mathematical capabilities.",
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard includes several mathematics-specific benchmarks, focusing particularly on grade school and advanced mathematics.",
                "analysis_tips": [
                    "This leaderboard only includes open models, so you won't find proprietary models here.",
                    "Pay attention to both raw and processed scores for math benchmarks.",
                    "Consider performance across different difficulty levels.",
                    "Look for models that excel at both computation and mathematical reasoning."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "MATH Lvl 5",
                        "benchmark_measures": "Evaluates performance on advanced mathematical problems at a high difficulty level.",
                        "score_interpretation": "Higher scores indicate better advanced mathematical capabilities.",
                    },
                    {
                        "benchmark_name": "MATH Lvl 5 Raw",
                        "benchmark_measures": "Provides unprocessed scores from Level 5 MATH dataset evaluations.",
                        "score_interpretation": "Higher scores reflect better raw performance on advanced mathematics.",
                    },
                    {
                        "benchmark_name": "GSM8K",
                        "benchmark_measures": "Evaluates ability to solve grade school math word problems.",
                        "score_interpretation": "Higher scores indicate better practical math problem-solving ability.",
                    }
                ]
            },
            {
                "leaderboard": "MathEval",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://matheval.ai/en/leaderboard/"
                },
            },
        ],
        "Convert speech to text": [
            {
                "leaderboard": "Artificial Analysis STT",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/speech-to-text"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for speech-to-text capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "Higher scores indicate better performance across all metrics.",
                    "Consider both accuracy and speed metrics for production use.",
                    "Compare performance across different audio quality levels.",
                    "Look at real-world performance rather than just ideal conditions.",
                    "Use their interactive visualizations to compare models directly."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Transcription Accuracy",
                        "benchmark_measures": "Evaluates overall accuracy of speech recognition across various conditions.",
                        "score_interpretation": "Higher scores indicate better transcription accuracy.",
                    },
                    {
                        "benchmark_name": "Real-World Robustness",
                        "benchmark_measures": "Assesses performance in challenging real-world conditions.",
                        "score_interpretation": "Higher scores indicate better handling of real-world scenarios.",
                    },
                    {
                        "benchmark_name": "Processing Efficiency",
                        "benchmark_measures": "Evaluates the speed and resource usage of speech recognition.",
                        "score_interpretation": "Higher scores indicate more efficient processing.",
                    },
                    {
                        "benchmark_name": "Specialized Content",
                        "benchmark_measures": "Tests accuracy on domain-specific and technical content.",
                        "score_interpretation": "Higher scores indicate better specialized content handling.",
                    }
                ]
            },
    ],
        "Convert text to speech": [
            {
                "leaderboard": "Artificial Analysis TTS",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-speech"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for text-to-speech capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "Higher scores indicate better performance across all metrics.",
                    "Consider both quality and speed metrics for production use.",
                    "Pay attention to cost implications alongside performance.",
                    "Compare performance between real-time and non-real-time models.",
                    "Use their interactive visualizations to compare models directly."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Voice Naturalness",
                        "benchmark_measures": "Evaluates how natural and human-like the synthesized speech sounds.",
                        "score_interpretation": "Higher scores indicate more natural-sounding speech.",
                    },
                    {
                        "benchmark_name": "Voice Clarity",
                        "benchmark_measures": "Assesses the clarity and intelligibility of synthesized speech.",
                        "score_interpretation": "Higher scores indicate clearer speech output.",
                    },
                    {
                        "benchmark_name": "Processing Speed",
                        "benchmark_measures": "Evaluates the time taken to generate speech from text input.",
                        "score_interpretation": "Higher scores indicate faster processing.",
                    },
                    {
                        "benchmark_name": "Speaker Consistency",
                        "benchmark_measures": "Evaluates the model's ability to maintain consistent voice characteristics.",
                        "score_interpretation": "Higher scores indicate better consistency.",
                    }
                ]
            },
            ], # End of Text to Speech (TTS) tasks
    },
    "Speed": {
        "Analyze data", 
        "Chat", 
        "Complex reasoning",  
        "Generate code", 
        "Generate images", 
        "Generate text", 
        "Generate video"
        "Math", 
        "Speech to text", 
        "Text to speech" 
    },
    "Latency": {
        "Analyze data", 
        "Chat", 
        "Complex reasoning",  
        "Generate code", 
        "Generate images", 
        "Generate text", 
        "Generate video"
        "Math", 
        "Speech to text", 
        "Text to speech" 
    },
    "Cost": {
        "Analyze data", 
        "Chat", 
        "Complex reasoning",  
        "Generate code", 
        "Generate images", 
        "Generate text", 
        "Generate video"
        "Math", 
        "Speech to text", 
        "Text to speech" 
    },
    "Context Window": {
        "Analyze data", 
        "Chat", 
        "Complex reasoning",  
        "Generate code", 
        "Generate images", 
        "Generate text", 
        "Generate video"
        "Math", 
        "Speech to text", 
        "Text to speech" 
    }
}





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
