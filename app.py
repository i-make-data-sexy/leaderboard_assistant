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
                    "You can sort the table by each column.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "metrics": [
                    {
                        "metric_name": "Overall",
                        "metric_measures": "The general ranking of the model across all task categories.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Based on pairwise comparisons between models",
                            "Uses Bradley-Terry model for ranking",
                            "Aggregates results across all categories",
                            "Considers both expert and general user evaluations",
                            "Updated in real-time with new comparisons"
                        ],
                        "ex_questions": [
                            "Explain quantum computing to a high school student.",
                            "Write a short story about a robot learning to paint.",
                            "What are the key differences between REST and GraphQL?"
                        ]
                    },
                    {
                        "metric_name": "Overall w/ Style Control",
                        "metric_measures": "Ranking considering the model's ability to maintain stylistic consistency in its responses.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Evaluates consistency in writing style",
                            "Tests ability to maintain specified tone",
                            "Measures adaptability to different personas",
                            "Assesses coherence across long responses",
                            "Includes style-specific prompting"
                        ],
                        "ex_questions": [
                            "Explain blockchain technology in the style of Shakespeare.",
                            "Write a technical documentation in a casual, friendly tone.",
                            "Describe machine learning like you're talking to a 5-year-old."
                        ]
                    },
                    {
                        "metric_name": "Hard Prompts (Overall)",
                        "metric_measures": "Model performance on challenging or complex prompts.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Uses specially crafted challenging prompts",
                            "Tests multi-step reasoning abilities",
                            "Includes edge cases and corner scenarios",
                            "Evaluates handling of ambiguous instructions",
                            "Assesses response to conflicting requirements"
                        ],
                        "ex_questions": [
                            "Design a system that handles both metric and imperial measurements while considering international date line complications.",
                            "Explain how to implement a distributed consensus algorithm while considering network partitions.",
                            "Create a strategy for optimizing a multi-variable function with competing constraints."
                        ]
                    },
                    {
                        "metric_name": "Hard Prompts w/ Style Control",
                        "metric_measures": "Model's ranking on hard prompts, also considering style consistency.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Combines hard prompt evaluation with style control",
                            "Tests maintenance of consistent voice in complex scenarios",
                            "Evaluates adaptation to multiple constraints",
                            "Assesses style flexibility under pressure",
                            "Measures coherence in challenging contexts"
                        ],
                        "ex_questions": [
                            "Explain quantum entanglement in the style of a noir detective novel.",
                            "Write a technical analysis of a distributed system in the voice of a sports commentator.",
                            "Describe a complex algorithm using only words a middle school student would understand."
                        ]
                    },
                    {
                        "metric_name": "Instruction Following",
                        "metric_measures": "How well the model follows explicit user instructions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Evaluates precise adherence to instructions",
                            "Tests handling of multi-step directions",
                            "Measures attention to constraints",
                            "Assesses completion of all requirements",
                            "Checks for instruction violation rates"
                        ],
                        "ex_questions": [
                            "Write a recipe that uses exactly 7 ingredients, with steps numbered 1-5, and include cooking time in minutes.",
                            "Create a list of 3 movie recommendations, each with exactly one sentence plot summary and a year.",
                            "Generate a haiku about technology that includes the word 'digital' in the second line."
                        ]
                    },
                    {
                        "metric_name": "Coding",
                        "metric_measures": "Model's ability to understand and generate code effectively.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests code generation capabilities",
                            "Evaluates code explanation skills",
                            "Assesses debugging abilities",
                            "Measures code optimization skills",
                            "Tests multiple programming languages",
                            "Evaluates documentation quality"
                        ],
                        "ex_questions": [
                            "Write a Python function that implements a binary search tree with insert and delete methods.",
                            "Debug this JavaScript code that should sort an array but produces incorrect results.",
                            "Optimize this SQL query that's running slowly on a large dataset."
                        ]
                    },
                    {
                        "metric_name": "Math",
                        "metric_measures": "Model's accuracy in solving mathematical problems.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Covers various mathematical domains",
                            "Tests step-by-step problem solving",
                            "Evaluates symbolic manipulation",
                            "Assesses mathematical reasoning",
                            "Includes word problems and pure math",
                            "Tests different difficulty levels"
                        ],
                        "ex_questions": [
                            "Solve for x: log(x^2 - 5x + 6) = 2.",
                            "A train travels at 60 mph for 2.5 hours, then 45 mph for 1.5 hours. What's the average speed?",
                            "Find the area of intersection between two circles with radii 5 and 3, centers 4 units apart."
                        ]
                    },
                    {
                        "metric_name": "Multi-Turn",
                        "metric_measures": "Model's performance in multi-turn conversations, reflecting conversational consistency and coherence.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Evaluates conversation continuity",
                            "Tests context retention across turns",
                            "Assesses reference resolution",
                            "Measures consistency in long dialogues",
                            "Tests handling of topic switches",
                            "Evaluates memory of previous context"
                        ],
                        "ex_questions": [
                            "Let's plan a vacation. Start by asking about my preferences, then make suggestions based on my answers.",
                            "Help me debug my code. I'll share the error message first, then we'll work through possible solutions.",
                            "Let's play a riddle game where you give hints and I try to guess the answer."
                        ]
                    },
                    {
                        "metric_name": "Longer Query",
                        "metric_measures": "Effectiveness in handling and responding accurately to longer, more complex queries.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests processing of lengthy inputs",
                            "Evaluates attention to detail",
                            "Measures completion of all requirements",
                            "Assesses information organization",
                            "Tests handling of multiple topics",
                            "Evaluates response comprehensiveness"
                        ],
                        "ex_questions": [
                            "Review this 3-page technical document and identify all security vulnerabilities while suggesting improvements and prioritizing them by risk level.",
                            "Analyze this customer feedback dataset containing 50 responses and provide key themes, sentiment analysis, and specific improvement recommendations.",
                            "Compare and contrast three different machine learning approaches for time series prediction, including their assumptions, computational requirements, and typical use cases."
                        ]
                    },
                    {
                        "metric_name": "Arena Score",
                        "metric_measures": "Ranks based on LLM performance in head-to-head comparisons. This score is derived using the Elo rating system, a method traditionally employed in chess and other competitive games to assess the relative skill levels of players.",
                        "score_interpretation": "Score ranges from 1 – thousands (higher is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Based on Elo rating system from chess",
                            "Updates dynamically after each comparison",
                            "Accounts for opponent strength",
                            "Considers win/loss patterns",
                            "Adjusts ratings based on expected performance",
                            "Maintains relative skill distances between models"
                        ],
                        "ex_questions": [
                            "Compare these two responses and select which is better: [Response A] vs [Response B].",
                            "Which model provides a more accurate and detailed explanation of quantum mechanics?",
                            "Which response better follows the user's instructions while maintaining natural language?"
                        ]
                    },
                    {
                        "metric_name": "Multilingual Maths (MGSM)",
                        "metric_measures": "Evaluates the model's ability to solve mathematical problems presented in multiple languages, testing both quantitative reasoning and multilingual comprehension.",
                        "score_interpretation": "Higher scores indicate better performance in solving math problems across diverse languages, reflecting both mathematical accuracy and multilingual capabilities.",
                        "metric_origin": "MGSM Research Team",
                        "metric_details": [
                            "Problems presented in multiple languages",
                            "Tests mathematical reasoning across languages",
                            "Evaluates consistency of solutions",
                            "Assesses language-independent problem solving",
                            "Includes various mathematical concepts",
                            "Validates translation accuracy"
                        ],
                        "ex_questions": [
                            "Solve this geometry problem presented in both Mandarin and English: Find the area of a triangle with base 6cm and height 8cm.",
                            "Calculate la somme de la série: 1 + 1/2 + 1/4 + 1/8 + ... jusqu'à l'infini (Calculate the sum of the series in French).",
                            "Решите уравнение: 3x + 5 = 20 (Solve the equation in Russian)."
                        ]   
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
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.", 
                    "Under their 'Quality Evaluations' section, they only show 15 of the available 81 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
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
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate better performance.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Combines multiple performance indicators",
                            "Weights different aspects of model performance",
                            "Includes task-specific evaluations",
                            "Normalizes scores across different scales",
                            "Updates regularly with new model versions"
                        ],
                        "ex_questions": [
                            "Create a comprehensive marketing strategy for a new eco-friendly product line.",
                            "Develop a lesson plan for teaching basic probability to high school students.",
                            "Write a detailed analysis of the impact of social media on modern journalism."
                        ]
                    },
                    {
                        "metric_name": "Reasoning & Knowledge (MMLU)",
                        "metric_measures": "Measures the model's ability to answer questions across 57 academic subjects, testing both reasoning and world knowledge.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate better performance, reflecting a stronger ability to reason and recall factual information.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Tests 57 different academic and professional subjects",
                            "15,908 total multiple-choice questions",
                            "Each subject has ~279 questions on average",
                            "Questions from real academic tests and professional exams",
                            "4-choice multiple choice format",
                            "Zero-shot and few-shot evaluation settings"
                        ],
                        "ex_questions": [
                            "Which psychologist is known for developing the hierarchy of needs? A) Freud B) Maslow C) Jung D) Skinner",
                            "What is the main function of mitochondria in cells? A) Protein synthesis B) Energy production C) DNA storage D) Cell division",
                            "In which year was the United Nations founded? A) 1943 B) 1944 C) 1945 D) 1946"
                        ]
                    },
                    {
                        "metric_name": "Scientific Reasoning & Knowledge (GPQA Diamond)",
                        "metric_measures": "Evaluates the model's ability to answer questions requiring scientific reasoning, logical problem-solving, and subject-specific expertise.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate better performance, indicating superior scientific understanding and problem-solving accuracy.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Focuses on scientific concepts and principles",
                            "Tests application of scientific method",
                            "Evaluates experimental design understanding",
                            "Assesses data interpretation skills",
                            "Includes cross-disciplinary problems",
                            "Tests both theory and practical application"
                        ],
                        "ex_questions": [
                            "Design an experiment to test the effect of temperature on enzyme activity.",
                            "Explain why the sky appears blue using principles of physic.s",
                            "Calculate the molarity of a solution made by dissolving 40g of NaOH in 500mL of water."
                        ]
                    },
                    {
                        "metric_name": "Quantitative Reasoning (MATH)",
                        "metric_measures": "Tests the model's mathematical reasoning and problem-solving skills, including algebra, calculus, and number theory.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate better performance, i.e., higher mathematical reasoning and accuracy.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        # Using same metric_details as MATH from previous leaderboard
                        "metric_details": [
                            "Covers various mathematical domains",
                            "Tests step-by-step problem solving",
                            "Evaluates symbolic manipulation",
                            "Assesses mathematical reasoning",
                            "Includes word problems and pure math",
                            "Tests different difficulty levels"
                        ],
                        "ex_questions": [
                            "Find the derivative of f(x) = x^3 * ln(x) using the product rule.",
                            "If a sequence follows the pattern an = an-1 + an-2 with a1 = 1 and a2 = 2, what is a6?",
                            "Solve the system of equations: 2x + 3y = 12 and 4x - y = 5"
                        ]
                    },
                    {
                        "metric_name": "Coding (HumanEval)",
                        "metric_measures": "Evaluates the model's ability to generate syntactically correct and functional code based on problem statements.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate greater coding proficiency and correctness.",
                        "metric_origin": "OpenAI Research",
                        "metric_details": [
                            "Tests code generation capabilities",
                            "Evaluates code explanation skills",
                            "Assesses debugging abilities",
                            "Measures code optimization skills",
                            "Tests multiple programming languages",
                            "Evaluates documentation quality"
                        ],
                        "ex_questions": [
                            "Create a function that implements the QuickSort algorithm for sorting an array.",
                            "Write a class that implements a thread-safe producer-consumer queue.",
                            "Implement a function to find the longest common subsequence of two strings."
                        ]
                    },
                    {
                        "metric_name": "Communication (LMSys Chatbot Arena ELO Score)",
                        "metric_measures": "Measures the model's performance in conversational settings, evaluating communication skills, coherence, and engagement based on user feedback.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate superior conversational ability, as judged by one-to-one comparisons.",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Evaluates natural conversation flow",
                            "Tests contextual understanding",
                            "Measures response relevance",
                            "Assesses personality consistency",
                            "Tests emotional intelligence",
                            "Evaluates cultural awareness",
                            "Measures conversation memory"
                        ],
                        "ex_questions": [
                            "Explain quantum computing to a high school student, adapting your explanation based on their follow-up questions.",
                            "Help a user troubleshoot a technical problem, maintaining empathy while gathering necessary information.",
                            "Engage in a discussion about climate change, acknowledging different viewpoints while providing accurate information."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard only includes open models, so you won't find performance metrics for proprietary models here (e.g., OpenAI, Google, Anthropic, etc).",
                "analysis_tips": [
                    "I'll be honest. This is my least favorite leaderboard. It's not as user-friendly as the others. It's very busy and only includes a table at the time of writing.",
                    "It offers a total of 27 columns but only shows eight by default. Above the chart you can select which columns you want to display.",
                    "The whole reason I'm creating this tool is that none of the leaderboards make it easy to see how metrics are defined. But the sheer busyness of this leaderboard makes that oversight more glaring.",
                    "The What LLM Provider does a much better job visualizing the data from the Artificial Analysis leaderboard imo (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "metrics": [
                    {
                        "metric_name": "Average",
                        "metric_measures": "The overall average score across all evaluated tasks.",
                        "score_interpretation": "Higher scores indicate better overall performance.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Combines scores from all evaluation tasks",
                            "Normalizes different scoring scales",
                            "Weights all tasks equally",
                            "Updates with each new evaluation",
                            "Includes all benchmark categories"
                        ],
                        "ex_questions": [
                            "What factors impact the average performance most significantly?",
                            "How do different model sizes affect the overall average?",
                            "What's the correlation between model parameters and average performance?"
                        ]
                    },
                    {
                        "metric_name": "IFEval",
                        "metric_measures": "Evaluates the model's instruction-following capability.",
                        "score_interpretation": "Higher scores indicate better adherence to instructions.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Tests precise instruction following",
                            "Evaluates multi-step direction handling",
                            "Measures constraint adherence",
                            "Assesses completion accuracy",
                            "Tracks instruction violation rates"
                        ],
                        "ex_questions": [
                            "Create a numbered list of capitals, but only for countries starting with 'B'.",
                            "Write a summary of climate change using exactly 50 words.",
                            "Generate a recipe that uses no dairy products and takes less than 30 minutes."
                        ]
                    },
                    {
                        "metric_name": "IFEval Raw",
                        "metric_measures": "The unprocessed or raw scores from instruction-following evaluations.",
                        "score_interpretation": "Higher scores reflect better raw instruction-following performance.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Unprocessed instruction following scores",
                            "No normalization applied",
                            "Direct performance measurement",
                            "Includes all response variations",
                            "Raw success/failure counts",
                            "Maintains original scoring format"
                        ],
                        "ex_questions": [
                            "Write exactly five sentences about climate change without using the letter 'e'.",
                            "Generate a list of prime numbers between 1 and 100, formatting each on a new line.",
                            "Translate this paragraph into French, maintaining all original punctuation."
                        ]
                    },
                    {
                        "metric_name": "BBH",
                        "metric_measures": "Evaluates performance on challenging prompts from the Big-Bench Hard (BBH) dataset.",
                        "score_interpretation": "Higher scores reflect better handling of complex, nuanced tasks.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Collection of 23 challenging task categories",
                            "Tasks designed to be difficult for current models",
                            "Focus on multi-step reasoning",
                            "Includes logical reasoning, abstract thinking",
                            "Problems require complex problem decomposition"
                        ],
                        "ex_questions": [
                            "If all bloops are floops, and no floops are woops, can a bloop be a woop? Explain your reasoning.",
                            "Find the next number: 3, 7, 15, 31, ?, 127. Show your work.",
                            "A train leaves at 2pm going 60mph. Another leaves at 3pm going 75mph. When will they meet if they're 315 miles apart?"
                        ]
                    },
                    {
                        "metric_name": "BBH Raw",
                        "metric_measures": "The raw scores from the BBH dataset evaluation.",
                        "score_interpretation": "Higher scores indicate better raw performance on complex prompts.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Unprocessed BBH task scores",
                            "No adjustment for difficulty",
                            "Direct success/failure recording",
                            "Raw completion accuracy",
                            "Includes partial solutions",
                            "Maintains original scoring criteria"
                        ],
                        "ex_questions": [
                            "Solve this logical sequence without hints: Red, Blue, Yellow, Red, Blue, ?, ?, ?",
                            "Complete this pattern recognition task: 1, 3, 6, 10, 15, ?",
                            "Find the underlying rule: [4,2,8], [9,3,27], [5,2,10], [8,2,?]"
                        ]
                    },
                    {
                        "metric_name": "MATH Lvl 5",
                        "metric_measures": "Evaluates mathematical reasoning at a high (Level 5) difficulty.",
                        "score_interpretation": "Higher scores indicate better performance on advanced mathematical problems.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Covers various mathematical domains",
                            "Tests step-by-step problem solving",
                            "Evaluates symbolic manipulation",
                            "Assesses mathematical reasoning",
                            "Includes word problems and pure math",
                            "Tests different difficulty levels"
                        ],
                        "ex_questions": [
                            "Find all complex solutions to the equation z^4 + 4z^3 + 6z^2 + 4z + 1 = 0.",
                            "Prove that for any positive integer n, 5^n - 4^n is divisible by n.",
                            "Calculate the volume of the solid formed by rotating y = sin(x) from 0 to π around the x-axis."
                        ],
                    },
                    {
                        "metric_name": "MATH Lvl 5 Raw",
                        "metric_measures": "The raw, unprocessed scores from the Level 5 MATH dataset.",
                        "score_interpretation": "Higher scores reflect better raw mathematical problem-solving performance.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Unprocessed advanced math scores",
                            "No curve or scaling applied",
                            "Direct solution accuracy",
                            "Includes partial credit responses",
                            "Raw step-by-step evaluation",
                            "Original scoring guidelines"
                        ],
                        "ex_questions": [
                            "Find all values of x where (x²-4)/(x-2) is undefined. Show all work.",
                            "Prove that the sequence an = n²+1 is not arithmetic. Provide complete proof.",
                            "Solve the differential equation dy/dx = y² with y(0)=1 without simplification."
                        ]                       
                    },
                    {
                        "metric_name": "GPQA",
                        "metric_measures": "Evaluates performance on General Physics Question Answering tasks.",
                        "score_interpretation": "Higher scores indicate better accuracy in answering physics-related questions.",
                        "metric_origin": "AI2/Allen Institute for AI",
                        "metric_details": [
                            "Covers fundamental physics concepts",
                            "Tests problem-solving abilities",
                            "Includes numerical calculations",
                            "Assesses conceptual understanding",
                            "Ranges from mechanics to quantum physics"
                        ],
                        "ex_questions": [
                            "A satellite orbits Earth at 400km altitude. Calculate its orbital period.",
                            "Explain why a spinning gyroscope maintains its orientation in space.",
                            "Calculate the magnetic field strength 10cm from a wire carrying 5A current."
                        ]
                    },
                    {
                        "metric_name": "GPQA Raw",
                        "metric_measures": "The raw scores from GPQA evaluations.",
                        "score_interpretation": "Higher scores reflect better raw performance on physics-related questions.",
                        "metric_origin": "AI2/Allen Institute for AI",
                        "metric_details": [
                            "Unprocessed physics question scores",
                            "No adjustment for complexity",
                            "Direct answer evaluation",
                            "Includes numerical precision",
                            "Raw conceptual accuracy",
                            "Original grading criteria"
                        ],
                        "ex_questions": [
                            "Calculate the exact electric field 5cm from a point charge of 2μC without rounding.",
                            "Determine the precise wavelength of a photon with energy 2.5eV showing all work.",
                            "Find the raw acceleration of a mass on an inclined plane of 30° with μ=0.2."
                        ]
                    },
                    {
                        "metric_name": "MUSR",
                        "metric_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores reflect better ability to perform chained reasoning.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Tests complex reasoning chains",
                            "Evaluates logical deduction",
                            "Assesses intermediate step accuracy",
                            "Measures reasoning consistency",
                            "Includes diverse problem types"
                        ],
                        "ex_questions": [
                            "Plan a trip through 5 European cities optimizing for cost, time, and must-see attractions.",
                            "Debug a web application with three interconnected errors affecting different components.",
                            "Design a sustainable urban garden considering space, sunlight, water usage, and seasonal crops."
                        ]
                    },
                    {
                        "metric_name": "MUSR Raw",
                        "metric_measures": "The raw scores from MUSR evaluations.",
                        "score_interpretation": "Higher scores indicate better raw performance in chained reasoning tasks.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Unprocessed multi-step reasoning scores",
                            "No normalization of results",
                            "Raw step completion accuracy",
                            "Direct logic chain evaluation",
                            "Includes all reasoning steps",
                            "Original scoring format"
                        ],
                        "ex_questions": [
                            "Show all steps to optimize a delivery route for 5 locations with different time windows without simplification.",
                            "Provide complete reasoning chain for solving a murder mystery with 6 suspects and 4 pieces of evidence.",
                            "Detail every step in designing a garden that maximizes yield given constraints on water, sunlight, and space."
                        ]
                    },
                    {
                        "metric_name": "MMLU-PRO",
                        "metric_measures": "Evaluates professional-level reasoning and knowledge across diverse subjects.",
                        "score_interpretation": "Higher scores reflect better reasoning at a professional level.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Focuses on professional and advanced academic subjects",
                            "Includes specialized domain knowledge",
                            "Tests graduate-level concepts",
                            "Covers professional certifications material",
                            "Evaluates expert-level reasoning",
                            "Includes industry-specific scenarios"
                        ],
                        "ex_questions": [
                            "In corporate law, explain the business judgment rule and its implications for director liability.",
                            "Describe the mechanism of action for selective serotonin reuptake inhibitors (SSRIs).",
                            "Explain how quantum tunneling affects the operation of flash memory devices."
                        ]
                    },
                    {
                        "metric_name": "MMLU-PRO Raw",
                        "metric_measures": "The raw scores from professional-level MMLU evaluations.",
                        "score_interpretation": "Higher scores indicate better raw performance in professional-level reasoning.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Unprocessed scores from MMLU-PRO",
                            "No scaling or normalization applied",
                            "Direct performance measurements",
                            "Includes all response data",
                            "Maintains original scoring format",
                            "Preserves statistical distributions"
                        ],
                        "ex_questions": [
                            "What is the primary mechanism of RNA splicing? A) Exon joining B) Intron removal C) Base pairing D) Nucleotide addition",
                            "In financial derivatives, what is the put-call parity relationship? [Technical options provided].",
                            "Explain the differences between L1 and L2 regularization in machine learning [Detailed technical response required]."
                        ]
                    },
                    {
                        "metric_name": "CO₂ cost (kg)",
                        "metric_measures": "Measures the carbon footprint of running the model in kilograms of CO₂.",
                        "score_interpretation": "Lower scores indicate more environmentally efficient models.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Calculates total energy consumption",
                            "Converts to CO₂ equivalent emissions",
                            "Considers data center efficiency",
                            "Measures training and inference costs",
                            "Accounts for hardware utilization",
                            "Includes cooling system impact"
                        ],
                        "ex_questions": [
                            "Calculate the CO₂ emissions for training a model with 1 billion parameters for 24 hours.",
                            "Compare the carbon footprint of inference across different model sizes and batch sizes.",
                            "Estimate the environmental impact of fine-tuning versus training from scratch."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page.",
                    "I really like that this leaderboard includes cutoff dates. Most do not.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "metrics": [
                    {
                        "metric_name": "Average",
                        "metric_measures": "The overall average score across all evaluated tasks, providing a general performance indicator.",
                        "score_interpretation": "Higher scores reflect better overall performance.",
                        "metric_origin": "Vellum AI Research Team",
                        "metric_details": [
                            "Combines all benchmark scores",
                            "Equal weighting across tasks",
                            "Normalized to consistent scale",
                            "Updated with new evaluations",
                            "Includes all test categories",
                            "Standardized scoring format"
                        ],
                        "ex_questions": [
                            "How does model size correlate with average performance across all benchmarks?",
                            "What is the performance trend across different model architectures?",
                            "Compare performance stability across different tasks and domains."
                        ]
                    },
                    {
                        "metric_name": "Multi-choice Qs",
                        "metric_measures": "Vellum's label for the MMLU Benchmark. Measures the model's ability to answer multiple-choice questions across 57 academic subjects, evaluating both reasoning and general world knowledge.",
                        "score_interpretation": "Higher scores indicate better reasoning and accuracy.",
                        "metric_origin": "Hendrycks et al., UC Berkeley (MMLU)",
                        "metric_details": [
                            "Tests 57 different academic and professional subjects",
                            "15,908 total multiple-choice questions",
                            "Each subject has ~279 questions on average",
                            "Questions from real academic tests and professional exams",
                            "4-choice multiple choice format",
                            "Zero-shot and few-shot evaluation settings"
                        ],
                        "ex_questions": [
                            "Which hormone is primarily responsible for blood glucose regulation? A) Insulin B) Glucagon C) Cortisol D) Thyroxine",
                            "Who wrote 'The Republic'? A) Aristotle B) Plato C) Socrates D) Herodotus",
                            "What is the primary function of RAM in a computer? A) Long-term storage B) Processing C) Temporary memory D) Data encryption"
                        ]
                    },
                    {
                        "metric_name": "Reasoning",
                        "metric_measures": "Vellum's label for the HellaSwag Benchmark. Assesses the model's commonsense reasoning and ability to predict plausible next steps in a scenario.",
                        "score_interpretation": "Higher scores denote better commonsense reasoning capabilities.",
                        "metric_origin": "HellaSwag Research Team",
                        "metric_details": [
                            "Tests common sense understanding",
                            "Evaluates situational reasoning",
                            "Assesses narrative comprehension",
                            "Measures contextual awareness",
                            "Includes diverse scenarios",
                            "Tests real-world knowledge"
                        ],
                        "ex_questions": [
                            "Complete the sequence: The chef put the cake in the oven, then...",
                            "What would likely happen if you left an ice cream cone in the sun?",
                            "Why might someone bring an umbrella to work on a sunny day?"
                        ]
                    },
                    {
                        "metric_name": "Python coding",
                        "metric_measures": "Vellum's label for the HumanEval Benchmark. Evaluates the model's ability to generate correct Python code from problem statements.",
                        "score_interpretation": "Higher scores reflect greater proficiency in coding tasks.",
                        "metric_origin": "OpenAI Research (HumanEval)",
                        "metric_details": [
                            "Tests code generation capabilities",
                            "Evaluates code explanation skills",
                            "Assesses debugging abilities",
                            "Measures code optimization skills",
                            "Tests multiple programming languages",
                            "Evaluates documentation quality"
                        ],
                        "ex_questions": [
                            "Write a Python function that finds the longest palindromic substring in a given string.",
                            "Create a decorator that caches function results and invalidates after a specified time period.",
                            "Implement a custom iterator class that generates prime numbers up to a given limit."
                        ]
                    },
                    {
                        "metric_name": "Future Capabilities",
                        "metric_measures": "Vellum's label for the BBHard Benchmark. Tests the model's performance on nuanced and challenging prompts from the Big-Bench Hard dataset.",
                        "score_interpretation": "Higher scores reflect better handling of complex and nuanced tasks.",
                        "metric_origin": "Google Research (BBH)",
                        "metric_details": [
                            "Collection of 23 challenging task categories",
                            "Tasks designed to be difficult for current models",
                            "Focus on multi-step reasoning",
                            "Includes logical reasoning, abstract thinking",
                            "Problems require complex problem decomposition",
                            "Tests advanced cognitive capabilities"
                        ],
                        "ex_questions": [
                            "If you stack 5 identical cubes in a way that each cube touches exactly two others, how many different arrangements are possible?",
                            "Design a system for fairly distributing limited resources among competing needs, considering both efficiency and equity.",
                            "Create a strategy for teaching a complex skill to someone who learns in an entirely different way than you do."
                        ]
                    },
                    {
                        "metric_name": "Grade school math",
                        "metric_measures": "Vellum's label for the GSM-8k Benchmark. Evaluates the model's ability to solve grade school-level math word problems.",
                        "score_interpretation": "Higher scores indicate better problem-solving accuracy.",
                        "metric_origin": "OpenAI Research (GSM-8k)",
                        "metric_details": [
                            "Contains grade school level problems",
                            "Tests basic arithmetic operations",
                            "Includes word problem interpretation",
                            "Assesses step-by-step reasoning",
                            "Covers practical applications",
                            "Evaluates problem comprehension"
                        ],
                        "ex_questions": [
                            "Sally has 3 bags of marbles. Each bag has twice as many marbles as the previous bag. If the first bag has 4 marbles, how many marbles does Sally have in total?",
                            "A restaurant serves 45 customers per hour. How many customers will they serve in a 7.5-hour shift?",
                            "If a rectangle's length is 3 times its width, and its perimeter is 64 inches, what is its area?"
                        ]
                    },
                    {
                        "metric_name": "Math problems",
                        "metric_measures": "Vellum's label for the MATH Benchmark. Assesses mathematical reasoning and accuracy on advanced topics such as algebra and calculus.",
                        "score_interpretation": "Higher scores denote better performance in complex mathematical reasoning.",
                        "metric_origin": "Hendrycks et al. (MATH)",
                        "metric_details": [
                            "Covers various mathematical domains",
                            "Tests step-by-step problem solving",
                            "Evaluates symbolic manipulation",
                            "Assesses mathematical reasoning",
                            "Includes word problems and pure math",
                            "Tests different difficulty levels"
                        ],
                        "ex_questions": [
                            "Find all values of x that satisfy the equation: log₂(x²-1) = 3",
                            "Prove that the sum of the first n odd numbers is equal to n².",
                            "A sphere is inscribed in a cube. If the cube's volume is 64 cubic units, what is the volume of the sphere?"
                        ]
                    }
                ]
            }
        ],
        "Code": [
            {
                "leaderboard": "BigCodeBench Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://bigcode-bench.github.io/"
                },
                "paper": {
                    "text": "Nerdy details 🤓",
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
                "metrics": [
                    {
                        "metric_name": "Calibrated Pass@1",
                        "metric_measures": "Adjusts the raw Pass@1 metric by accounting for common omissions or minor errors in code, such as missing imports or boilerplate. It measures the likelihood of a model generating code that solves a task correctly with slight, acceptable deviations.",
                        "score_interpretation": "Higher scores indicate better performance, emphasizing usability and real-world applicability over strict correctness.",
                        "metric_origin": "BigCode Research Team",
                        "metric_details": [
                            "Accounts for common code omissions",
                            "Considers functional equivalence",
                            "Tolerates minor syntax variations",
                            "Evaluates practical usability",
                            "Assesses intent matching",
                            "Includes real-world considerations"
                        ],
                        "ex_questions": [
                            "Write a function to implement a binary search tree with missing import statements.",
                            "Create a web scraper that works but might need additional error handling.",
                            "Implement a sorting algorithm with correct logic but incomplete type hints."
                        ]
                    },
                    {
                        "metric_name": "Pass@1 (Raw)",
                        "metric_measures": "The percentage of tasks solved correctly by the first attempt, without calibration for omissions or partial correctness.",
                        "score_interpretation": "Higher scores indicate stricter correctness with no allowance for omissions.",
                        "metric_origin": "BigCode Research Team",
                        "metric_details": [
                            "Strict correctness evaluation",
                            "No leniency for minor errors",
                            "Requires complete solutions",
                            "Tests exact specification matching",
                            "Includes all edge cases",
                            "Demands proper syntax"
                        ],
                        "ex_questions": [
                            "Implement a perfectly formatted Red-Black tree with complete error handling.",
                            "Create a fully documented REST API endpoint with all edge cases covered.",
                            "Write a complete matrix multiplication algorithm with input validation."
                        ]
                    },
                    {
                        "metric_name": "Pass@k (k=5, 10)",
                        "metric_measures": "The percentage of tasks for which at least one of the top-k generated solutions is correct.",
                        "score_interpretation": "Higher scores indicate better overall task-solving ability across multiple attempts.",
                        "metric_origin": "BigCode Research Team",
                        "metric_details": [
                            "Evaluates multiple solution attempts",
                            "Considers solution diversity",
                            "Measures consistency",
                            "Tests different approaches",
                            "Assesses solution quality distribution",
                            "Rewards robust problem-solving"
                        ],
                        "ex_questions": [
                            "Generate 5 different approaches to implementing a cache with different trade-offs.",
                            "Provide 10 variations of a function to calculate Fibonacci numbers.",
                            "Create multiple implementations of a parallel processing solution."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "CodeXGLUE Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://microsoft.github.io/CodeXGLUE/"
                },
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2102.04664"
                },
                "tooltip": "CodeXGLUE is a benchmark suite for code intelligence developed by Microsoft Research. It includes multiple tasks focused on code understanding and generation across various programming languages.",
                "analysis_tips": [
                    "The leaderboard is divided into different tasks. Check which specific task is most relevant to your needs.",
                    "Pay attention to the programming languages covered in each task.",
                    "Consider both accuracy and efficiency metrics when comparing models.",
                    "Note that some tasks focus on code understanding while others test code generation."
                ],
                "metrics": [
                        {
                            "metric_name": "Overall",
                            "metric_measures": "Aggregates performance across all CodeXGLUE tasks to evaluate general code intelligence capabilities",
                            "score_interpretation": "Higher scores indicate better overall performance across all benchmarks",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Combines scores from all sub-tasks",
                                "Normalizes across different metrics",
                                "Weights tasks appropriately",
                                "Considers multiple languages",
                                "Evaluates broad code intelligence",
                                "Balances different skill aspects"
                            ],
                            "ex_questions": [
                                "How does the model perform across all programming languages?",
                                "What's the aggregate performance across understanding and generation tasks?",
                                "How consistent is performance across different task types?"
                            ]
                        },
                        {
                            "metric_name": "Clone Detection (Code-Code)",
                            "metric_measures": "Identifies semantically equivalent code snippets despite syntactic differences",
                            "score_interpretation": "Higher F1 scores indicate better clone detection accuracy",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Evaluates semantic similarity detection",
                                "Tests across different programming languages",
                                "Measures precision and recall",
                                "Considers code structure",
                                "Accounts for variable renaming",
                                "Assesses functional equivalence"
                            ],
                            "ex_questions": [
                                "Determine if these two Java functions are semantically equivalent despite different variable names.",
                                "Identify if this Python implementation is a clone of this C++ code.",
                                "Detect if these two sorting implementations are functionally identical."
                            ]
                        },
                        {
                            "metric_name": "Defect Detection (Code-Code)",
                            "metric_measures": "Evaluates ability to identify bugs and potential defects in code",
                            "score_interpretation": "Higher accuracy indicates better defect detection",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Identifies various bug types",
                                "Tests security vulnerabilities",
                                "Assesses logical errors",
                                "Evaluates edge cases",
                                "Considers multiple languages",
                                "Measures false positive rate"
                            ],
                            "ex_questions": [
                                "Identify potential null pointer exceptions in this Java code.",
                                "Detect memory leaks in this C++ implementation.",
                                "Find SQL injection vulnerabilities in this database query."
                            ]
                        },
                        {
                            "metric_name": "Cloze Test (Code-Code)",
                            "metric_measures": "Tests understanding of code context by predicting masked tokens in code sequences",
                            "score_interpretation": "Higher accuracy scores indicate better token prediction ability",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Evaluates code context understanding",
                                "Tests token prediction accuracy",
                                "Assesses language model capabilities",
                                "Measures contextual awareness",
                                "Tests variable naming understanding",
                                "Evaluates syntax comprehension"
                            ],
                            "ex_questions": [
                                "Complete this Python function by filling in the missing control structure: 'for ___ in range(len(array))'",
                                "Predict the appropriate method name in: 'list.___(new_element)'",
                                "Fill in the missing type declaration in this TypeScript interface."
                            ]
                        },
                        {
                            "metric_name": "Code Completion (Code-Code)",
                            "metric_measures": "Measures ability to autocomplete partial code snippets with contextually appropriate suggestions",
                            "score_interpretation": "Higher accuracy and BLEU scores indicate better completion quality",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests line completion accuracy",
                                "Evaluates contextual relevance",
                                "Assesses syntax correctness",
                                "Measures completion speed",
                                "Tests multiple languages",
                                "Considers code style consistency"
                            ],
                            "ex_questions": [
                                "Complete this function signature based on its implementation: 'def sort_by_'",
                                "Suggest the next line in this React component after state initialization.",
                                "Complete this SQL query based on the table schema and previous queries."
                            ]
                        },
                        {
                            "metric_name": "Code Refinement (Code-Code)",
                            "metric_measures": "Evaluates capacity to improve code quality through bug fixes and optimizations",
                            "score_interpretation": "Higher accuracy and lower error rates indicate better refinement capabilities",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests optimization abilities",
                                "Evaluates bug fix accuracy",
                                "Assesses code quality improvements",
                                "Measures performance impact",
                                "Tests refactoring capabilities",
                                "Considers maintainability metrics"
                            ],
                            "ex_questions": [
                                "Optimize this function to reduce time complexity from O(n²) to O(n log n).",
                                "Refactor this code to follow SOLID principles.",
                                "Fix potential race conditions in this multithreaded implementation."
                            ]
                        },
                        {
                            "metric_name": "Code Translation (Code-Code)",
                            "metric_measures": "Tests ability to convert code between different programming languages while preserving functionality",
                            "score_interpretation": "Higher functional equivalence scores indicate better translation accuracy",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Evaluates semantic preservation",
                                "Tests cross-language understanding",
                                "Assesses idiomaticity",
                                "Measures performance equivalence",
                                "Tests language-specific features",
                                "Considers optimization levels"
                            ],
                            "ex_questions": [
                                "Translate this Python list comprehension to equivalent JavaScript array methods.",
                                "Convert this Java Spring controller to a Node.js Express route.",
                                "Transform this C++ template class into a Python generic class."
                            ]
                        },
                        {
                            "metric_name": "Type Prediction (Code-Code)",
                            "metric_measures": "Predicts variable and function types in dynamically typed languages",
                            "score_interpretation": "Higher accuracy indicates better type inference capabilities",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests type inference accuracy",
                                "Evaluates complex type recognition",
                                "Assesses generic type handling",
                                "Measures union type detection",
                                "Tests function signatures",
                                "Considers type hierarchies"
                            ],
                            "ex_questions": [
                                "Predict return types for these Python functions based on their implementations.",
                                "Infer parameter types in this JavaScript function from its usage.",
                                "Determine appropriate TypeScript interfaces for this object structure."
                            ]
                        },
                        {
                            "metric_name": "Natural Language Code Search (Text-Code)",
                            "metric_measures": "Evaluates effectiveness in finding relevant code snippets based on natural language queries",
                            "score_interpretation": "Higher MRR and NDCG scores indicate better search accuracy",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests search relevance",
                                "Evaluates semantic matching",
                                "Assesses ranking accuracy",
                                "Measures query understanding",
                                "Tests cross-language search",
                                "Considers code context"
                            ],
                            "ex_questions": [
                                "Find a function that implements binary search in any language.",
                                "Search for code that handles JWT authentication in Express.",
                                "Locate examples of database connection pooling patterns."
                            ]
                        },
                        {
                            "metric_name": "Code Generation (Text-Code)",
                            "metric_measures": "Evaluates ability to create executable code from natural language descriptions",
                            "score_interpretation": "Higher BLEU and exact match scores indicate better generation accuracy",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests code generation accuracy",
                                "Evaluates functional correctness",
                                "Assesses syntax validity",
                                "Measures requirement fulfillment",
                                "Tests edge case handling",
                                "Considers code efficiency"
                            ],
                            "ex_questions": [
                                "Create a function that sorts an array in descending order and removes duplicates.",
                                "Generate a REST API endpoint that handles user authentication.",
                                "Write a class that implements a priority queue with specified methods."
                            ]
                        },
                        {
                            "metric_name": "Code Summarization (Code-Text)",
                            "metric_measures": "Tests capacity to generate concise natural language descriptions of code functionality",
                            "score_interpretation": "Higher BLEU and ROUGE scores indicate better summarization quality",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Evaluates summary accuracy",
                                "Tests technical precision",
                                "Assesses conciseness",
                                "Measures completeness",
                                "Tests multiple languages",
                                "Considers code complexity"
                            ],
                            "ex_questions": [
                                "Explain what this recursive tree traversal algorithm does.",
                                "Summarize the functionality of this database transaction handler.",
                                "Describe the purpose and behavior of this state management hook."
                            ]
                        },
                        {
                            "metric_name": "Documentation Translation (Text-Text)",
                            "metric_measures": "Measures accuracy in translating technical documentation between different human languages",
                            "score_interpretation": "Higher BLEU scores indicate better translation quality",
                            "metric_origin": "Microsoft Research",
                            "metric_details": [
                                "Tests technical accuracy",
                                "Evaluates language fluency",
                                "Assesses terminology consistency",
                                "Measures context preservation",
                                "Tests multiple language pairs",
                                "Considers technical jargon"
                            ],
                            "ex_questions": [
                                "Translate this API documentation from English to Japanese while preserving technical terms.",
                                "Convert this Python package tutorial from Spanish to English.",
                                "Translate this deployment guide from German to Mandarin while maintaining formatting."
                            ]
                        }
                    ]  
            }
        ]
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
