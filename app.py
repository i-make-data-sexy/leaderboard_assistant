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
                # VERIFED   
                "leaderboard": "SEAL",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://scale.com/leaderboard/tool_use"
                },
                "tooltip": "",
                "analysis_tips": [],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": ""
                },
                "metrics": [
                    {
                        "metric_name": "Score",
                        "metric_measures": "Score calculates the mean of ToolComp-Enterprise and ToolComp-Chat. ToolComp-Enterprise assesses models on tasks requiring the use of 11 distinct tools, reflecting complex scenarios typical in enterprise settings. ToolComp-Chat evaluates models on tasks involving two common tools—Google Search and Python Interpreter—focusing on general-purpose chatbot capabilities.",
                        "score_interpretation": "Score ranges from 1 to 100 (higher is better).",
                        "metric_origin": "ToolComp",
                        "metric_details": [
                            "The ToolComp benchmark comprises 485 prompts & final answers designed to evaluate the proficiency of AI models in tasks necessitating dependent tool usage.",
                            "Define dependent tool calling as the need to call multiple tools in sequence such that the output of a previous tool must be used to motivate the input for a subsequent tool.",
                        ],
                        "ex_questions": [
                            "Suppose you have a 2 inch x 2 inch x 2 inch box. How many of these boxes can you fit into the biggest U-Haul truck (biggest truck as of 2024)?",
                            "Calculate the average daytime temperature in Paris during the week of Halloween (October 29th to November 4th, 2023). To plan accordingly, Sarah's family also wants to know the extreme temperatures experienced during this period. Specifically, what were the highest and lowest temperatures (in Fahrenheit) recorded in Paris during this time frame? Additionally, her family wants to know which date in this period had the lowest temperature as well the total hours of precipitation and the amount of rainfall (in mm) on that specific date.",
                            "Can you find Microsoft's stock price on the day before Windows XP was released and on the day of its release? Then, provide the percentage change between the two stock prices and the date difference between the two dates.",
                        ]
                    }
                ]
            },
            ],
        "Chat": [
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
                    "The introduction of their Arxiv paper (https://arxiv.org/html/2406.11939v2#S1) includes a table summary of how they collect their data for each benchmark (e.g., automatic or human), if the questions are open-ended, how prompts are curated (e.g., automatically, manually, or crowdsourced), and hte nature of the prompt source (e.g., configurable, fixed, or crowd).",
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
                        "metric_measures": "Evaluates performance on challenging prompts from the Big-bench Hard (BBH) dataset.",
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
                        "metric_measures": "Vellum's label for the BBHard Benchmark. Tests the model's performance on nuanced and challenging prompts from the BIG-bench Hard dataset.",
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
        "Solve complex problems": [
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://lmarena.ai/?leaderboard"
                },
                "tooltip": "The Chatbot Arena leaderboard includes specific evaluations of complex reasoning through human preference ratings.",
                "analysis_tips": [
                    "Pay special attention to the Hard Prompts metrics which test complex reasoning.",
                    "Consider Multi-Turn performance for extended reasoning chains.",
                    "Look for models that maintain logical consistency across longer responses.",
                    "Compare how models handle both structured and open-ended reasoning tasks."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2403.04132"
                },
                "metrics": [
                    {
                        "metric_name": "Hard Prompts (Overall)",
                        "metric_measures": "Evaluates performance on complex, multi-step reasoning challenges.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests logical deduction",
                            "Evaluates causal reasoning",
                            "Assesses problem decomposition",
                            "Measures argument analysis",
                            "Tests hypothesis generation",
                            "Evaluates evidence evaluation"
                        ],
                        "ex_questions": [
                            "Analyze the potential long-term consequences of implementing a universal basic income system.",
                            "Design a solution for reducing urban traffic that considers economic, social, and environmental factors.",
                            "Evaluate three competing theories about dark matter and explain which has the strongest evidence."
                        ]
                    },
                    {
                        "metric_name": "Multi-Turn Reasoning",
                        "metric_measures": "Tests ability to maintain logical consistency across extended reasoning chains.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests reasoning continuity",
                            "Evaluates premise tracking",
                            "Assesses logical flow",
                            "Measures assumption consistency",
                            "Tests inferential accuracy",
                            "Evaluates conclusion validity"
                        ],
                        "ex_questions": [
                            "Let's solve a complex murder mystery, step by step, evaluating each piece of evidence.",
                            "Help me diagnose a system failure by analyzing multiple potential causes and their interactions.",
                            "Guide me through designing a renewable energy system, considering multiple interconnected factors."
                        ]
                    },
                    {
                        "metric_name": "Complex Problem Solving",
                        "metric_measures": "Assesses ability to solve problems requiring multiple steps and consideration of various factors.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests strategic thinking",
                            "Evaluates trade-off analysis",
                            "Assesses solution optimization",
                            "Measures constraint handling",
                            "Tests scenario planning",
                            "Evaluates decision justification"
                        ],
                        "ex_questions": [
                            "Develop a strategy for a company to expand internationally while minimizing environmental impact.",
                            "Create a plan for evacuating a large city during a natural disaster, considering all critical factors.",
                            "Design an ethical framework for deploying autonomous vehicles in urban environments."
                        ]
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "metrics": [
                    {
                        "metric_name": "BBH (BIG-bench Hard)",
                        "metric_measures": "Evaluates performance on challenging prompts requiring complex reasoning.",
                        "score_interpretation": "Higher scores indicate better complex reasoning capabilities.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Tests multi-step reasoning",
                            "Evaluates novel problem-solving",
                            "Assesses abstract thinking",
                            "Measures strategic planning",
                            "Tests cognitive flexibility",
                            "Evaluates creative solutions"
                        ],
                        "ex_questions": [
                            "If all zorbs are plips, and no plips are woops, what can we conclude about zorbs and woops? Explain your reasoning.",
                            "Design a system that sorts objects by both color and size, handling edge cases like partially colored items.",
                            "Given these rules for a new board game, identify the optimal winning strategy."
                        ]
                    },
                    {
                        "metric_name": "BBH Raw",
                        "metric_measures": "Provides unprocessed scores from the BIG-bench Hard dataset evaluation.",
                        "score_interpretation": "Higher scores reflect better raw performance on complex reasoning tasks.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Shows unmodified scores",
                            "Tests pure reasoning ability",
                            "Assesses raw performance",
                            "Measures direct responses",
                            "Tests unadjusted accuracy",
                            "Evaluates baseline capabilities"
                        ],
                        "ex_questions": [
                            "Solve this logic puzzle without any hints or formatting adjustments.",
                            "Complete this pattern sequence using only first-principles reasoning.",
                            "Determine the next steps in this complex scenario without additional context."
                        ]
                    },
                    {
                        "metric_name": "MUSR",
                        "metric_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores indicate better sequential reasoning ability.",
                        "metric_origin": "HuggingFace Research Team",
                        "metric_details": [
                            "Tests step-by-step logic",
                            "Evaluates reasoning chains",
                            "Assesses intermediate steps",
                            "Measures solution pathways",
                            "Tests premise tracking",
                            "Evaluates conclusion validity"
                        ],
                        "ex_questions": [
                            "Plan a city's public transportation system, considering population growth, budget constraints, and environmental impact.",
                            "Develop a strategy for reducing food waste across a supply chain, addressing each stage systematically.",
                            "Analyze the potential effects of a new technology on different sectors of society, tracking interdependencies."
                        ]
                    },
                    {
                        "metric_name": "MUSR Raw",
                        "metric_measures": "Provides raw scores from multi-step reasoning evaluations.",
                        "score_interpretation": "Higher scores indicate better raw performance in sequential reasoning.",
                        "metric_origin": "HuggingFace Research Team",
                        "metric_details": [
                            "Records unprocessed results",
                            "Tests baseline reasoning",
                            "Assesses raw step accuracy",
                            "Measures direct performance",
                            "Tests sequential thinking",
                            "Evaluates pure logic"
                        ],
                        "ex_questions": [
                            "Break down this complex business problem into its component parts without guidance.",
                            "Trace the cause-and-effect relationships in this historical event using only available facts.",
                            "Map out the decision tree for this strategic planning scenario from first principles."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "BIG-bench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks"
                },
                "tooltip": "The Beyond the Imitation Game Benchmark (BIG-bench) includes extensive evaluations of complex reasoning capabilities.",
                "analysis_tips": [
                    "Focus on tasks that require multi-step reasoning processes.",
                    "Consider performance across different types of logical challenges.",
                    "Pay attention to both accuracy and explanation quality.",
                    "Look for models that can handle novel reasoning scenarios."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2206.04615"
                },
                "metrics": [
                    {
                        "metric_name": "Logical Deduction",
                        "metric_measures": "Tests ability to draw valid conclusions from given premises.",
                        "score_interpretation": "Higher scores indicate better logical reasoning capabilities.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Tests formal logic application",
                            "Evaluates deductive reasoning",
                            "Assesses syllogistic logic",
                            "Measures inference validity",
                            "Tests premise analysis",
                            "Evaluates conclusion soundness"
                        ],
                        "ex_questions": [
                            "Given that no cats are dogs and all pets in this house are cats, what can we conclude about dogs in this house?",
                            "If event A causes B, and B causes C, but C prevents A, analyze the logical paradox.",
                            "Using these three rules about a fictional society, determine which statements must be true."
                        ]
                    },
                    {
                        "metric_name": "Strategy QA",
                        "metric_measures": "Evaluates strategic thinking and multi-step planning abilities.",
                        "score_interpretation": "Higher scores indicate better strategic reasoning capabilities.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Tests strategic planning",
                            "Evaluates resource allocation",
                            "Assesses outcome prediction",
                            "Measures decision optimization",
                            "Tests contingency planning",
                            "Evaluates trade-off analysis"
                        ],
                        "ex_questions": [
                            "Design a strategy to maximize crop yield with limited water resources over five years.",
                            "Plan the most efficient way to evacuate a large building given specific constraints.",
                            "Develop a market entry strategy considering multiple competing factors."
                        ]
                    },
                    {
                        "metric_name": "Causal Reasoning",
                        "metric_measures": "Tests understanding of cause-and-effect relationships in complex systems.",
                        "score_interpretation": "Higher scores indicate better causal reasoning abilities.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Tests causality identification",
                            "Evaluates intervention effects",
                            "Assesses confounding factors",
                            "Measures chain reactions",
                            "Tests counterfactual thinking",
                            "Evaluates causal networks"
                        ],
                        "ex_questions": [
                            "Analyze how a change in interest rates affects different sectors of the economy.",
                            "Determine the likely root cause of multiple overlapping system failures.",
                            "Predict the cascading effects of removing a keystone species from an ecosystem."
                        ]
                    },
                    {
                        "metric_name": "Analogical Reasoning",
                        "metric_measures": "Assesses ability to transfer knowledge between different domains using analogies.",
                        "score_interpretation": "Higher scores indicate better analogical thinking capabilities.",
                        "metric_origin": "Google Research",
                        "metric_details": [
                            "Tests pattern matching",
                            "Evaluates conceptual mapping",
                            "Assesses structural similarity",
                            "Measures abstraction skills",
                            "Tests knowledge transfer",
                            "Evaluates analogy creation"
                        ],
                        "ex_questions": [
                            "Explain how the human immune system is like a country's defense system.",
                            "Compare the structure of a corporate hierarchy to another complex system.",
                            "Find analogous solutions between biological and technological systems."
                        ]
                    }
                ]
            },
            {
               "Leaderboard": "oobabooga",
               "Link": {
                   "text": "View leaderboard",
                   "url": "https://oobabooga.github.io/benchmark.html"
               },
               # ChatGPT thread: https://chatgpt.com/c/67589536-ab04-8002-8b22-b844466bc6af
            },
        ],
        "Generate code": [
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
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
                    "The table defaults to sorting by rank. I prefer to sort by Arena Score.",
                    "You can sort the table by the Coding column.",
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "metrics": [
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
                    "The Vellum leaderboard only has one chart for coding, 'Best in Coding (HumanEval)' with a meager five models (at the time of writing), but the Model Comparison table includes a benchmark called 'Python coding', which is their alias for HumanEval.",
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page.",
                    "I really like that this leaderboard includes cutoff dates. Most do not.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "metrics": [
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
                "tooltip": "The Chatbot Arena leaderboard includes specific metrics for evaluating creative and stylistic capabilities through human preference ratings.",
                "analysis_tips": [
                    "Focus on the Style Control metrics which evaluate creative capabilities.",
                    "The Overall w/ Style Control metric is particularly relevant for creative tasks.",
                    "Consider how models perform on longer-form content using the Longer Query metric.",
                    "Look for models that maintain high scores in both style and coherence metrics."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "metrics": [
                    {
                        "metric_name": "Overall w/ Style Control",
                        "metric_measures": "Evaluates the model's ability to maintain consistent creative style and tone across responses.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests stylistic consistency",
                            "Evaluates tone maintenance",
                            "Assesses voice authenticity",
                            "Measures creative adaptation",
                            "Tests genre adherence",
                            "Evaluates narrative coherence"
                        ],
                        "ex_questions": [
                            "Write a children's story about a brave robot in the style of Dr. Seuss.",
                            "Compose a noir-style detective story about a missing library book.",
                            "Create a science fiction narrative using Victorian-era language."
                        ]
                    },
                    {
                        "metric_name": "Longer Query",
                        "metric_measures": "Tests ability to maintain creative coherence and style in longer compositions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Evaluates sustained narratives",
                            "Tests plot development",
                            "Assesses character consistency",
                            "Measures story structure",
                            "Tests thematic coherence",
                            "Evaluates creative stamina"
                        ],
                        "ex_questions": [
                            "Write a three-act short story about a mysterious package that arrives on someone's doorstep.",
                            "Create a detailed character study of a person who discovers they can communicate with plants.",
                            "Compose a multi-scene story that takes place in different time periods."
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
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard includes metrics relevant to creative writing and text generation capabilities.",
                "analysis_tips": [
                    "Higher scores indicate better performance across all metrics.",
                    "Look for models that excel in both Quality Index and Communication scores for creative tasks.",
                    "Compare models' performance across different writing styles and formats.",
                    "Consider these quality scores alongside other performance metrics for a complete picture."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
                    {
                        "metric_name": "Quality Index",
                        "metric_measures": "Evaluates overall writing quality, including creativity, coherence, and engagement.",
                        "score_interpretation": "Higher scores indicate better overall writing quality.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests narrative coherence",
                            "Evaluates writing clarity",
                            "Assesses creative elements",
                            "Measures structural quality",
                            "Tests audience engagement",
                            "Evaluates stylistic consistency"
                        ],
                        "ex_questions": [
                            "Write a compelling opening paragraph for a novel about time travel.",
                            "Create a descriptive scene that establishes a specific mood without explicitly stating emotions.",
                            "Develop a dialogue that reveals character personality through speech patterns."
                        ]
                    },
                    {
                        "metric_name": "Communication",
                        "metric_measures": "Assesses effectiveness in conveying ideas and maintaining audience engagement.",
                        "score_interpretation": "Higher scores indicate better communication ability.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Evaluates clarity of expression",
                            "Tests audience adaptation",
                            "Measures narrative flow",
                            "Assesses rhetorical effectiveness",
                            "Tests voice consistency",
                            "Evaluates emotional resonance"
                        ],
                        "ex_questions": [
                            "Write a story that gradually reveals its twist through subtle foreshadowing.",
                            "Create a piece that effectively switches between past and present perspectives.",
                            "Compose a scene that conveys tension without explicitly mentioning conflict."
                        ]
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "metrics": [
                    {
                        "metric_name": "TruthfulQA - Writing",
                        "metric_measures": "Evaluates ability to generate accurate and engaging narrative content.",
                        "score_interpretation": "Higher scores indicate better writing accuracy and quality.",
                        "metric_origin": "Hugging Face Research Team",
                        "metric_details": [
                            "Tests factual integration",
                            "Evaluates creative storytelling",
                            "Assesses narrative accuracy",
                            "Measures content originality",
                            "Tests genre understanding",
                            "Evaluates source attribution"
                        ],
                        "ex_questions": [
                            "Write a historically accurate creative piece about the invention of the printing press.",
                            "Create a science fiction story that accurately incorporates quantum physics concepts.",
                            "Compose a biographical narrative that balances creativity with factual accuracy."
                        ]
                    }
                ]
            },
            # Add to the Creative Writing array:
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard offers simplified metrics relevant to creative writing and text generation capabilities.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them directly.",
                    "The last updated date is at the bottom of the page.",
                    "Vellum simplifies metric names for accessibility while maintaining technical rigor.",
                    "Consider how models perform across different narrative and descriptive tasks."
                ],
                "metrics": [
                    {
                        "metric_name": "Writing Style",
                        "metric_measures": "Evaluates the model's ability to maintain consistent tone and style in creative writing tasks.",
                        "score_interpretation": "Higher scores indicate better stylistic control and consistency.",
                        "metric_origin": "Vellum AI Research Team",
                        "metric_details": [
                            "Tests tone consistency",
                            "Evaluates voice adaptation",
                            "Measures stylistic flexibility",
                            "Assesses genre awareness",
                            "Tests narrative cohesion",
                            "Evaluates creative expression"
                        ],
                        "ex_questions": [
                            "Write a gothic horror story using Victorian-era language patterns.",
                            "Create a modern fairytale that maintains traditional storytelling elements.",
                            "Compose a technical topic explanation in a whimsical, engaging style."
                        ]
                    },
                    {
                        "metric_name": "Narrative Coherence",
                        "metric_measures": "Assesses the model's ability to maintain logical story flow and character consistency.",
                        "score_interpretation": "Higher scores denote better narrative structure and coherence.",
                        "metric_origin": "Vellum AI Research Team",
                        "metric_details": [
                            "Tests plot progression",
                            "Evaluates character consistency",
                            "Measures story structure",
                            "Assesses narrative logic",
                            "Tests scene transitions",
                            "Evaluates thematic unity"
                        ],
                        "ex_questions": [
                            "Write a story with multiple characters where their actions remain consistent with their established personalities.",
                            "Create a narrative that switches between three different time periods while maintaining a clear through-line.",
                            "Develop a story that reveals information gradually while maintaining reader engagement."
                        ]
                    },
                    {
                        "metric_name": "Creative Adaptation",
                        "metric_measures": "Tests ability to creatively adapt content for different audiences and purposes.",
                        "score_interpretation": "Higher scores indicate better creative flexibility and audience awareness.",
                        "metric_origin": "Vellum AI Research Team",
                        "metric_details": [
                            "Tests audience adaptation",
                            "Evaluates content transformation",
                            "Measures creative problem-solving",
                            "Assesses format flexibility",
                            "Tests genre translation",
                            "Evaluates tone adjustment"
                        ],
                        "ex_questions": [
                            "Rewrite a complex scientific concept as an engaging children's story.",
                            "Transform a serious historical event into a lighthearted but respectful narrative.",
                            "Adapt a traditional folktale into a modern setting while preserving its core message."
                        ]
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
                "tooltip": "The Chatbot Arena leaderboard includes specific evaluations of mathematical capabilities through human preference ratings.",
                "analysis_tips": [
                    "Check the Math-specific column for direct comparison of mathematical capabilities.",
                    "Consider models' ability to explain mathematical concepts, not just solve problems.",
                    "Look at Multi-Turn metrics for step-by-step problem solving ability.",
                    "Compare Arena Scores specifically for mathematics-focused prompts."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "metrics": [
                    {
                        "metric_name": "Math",
                        "metric_measures": "Evaluates the model's accuracy in solving mathematical problems.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests various mathematical domains",
                            "Evaluates step-by-step solutions",
                            "Assesses symbolic manipulation",
                            "Measures problem-solving strategies",
                            "Tests concept explanation ability",
                            "Evaluates error detection"
                        ],
                        "ex_questions": [
                            "Solve this differential equation: dy/dx = 2x + y with y(0) = 1.",
                            "Find the area of intersection between two circles with radii 5 and 3, centers 4 units apart.",
                            "Prove that the sequence an = n² + 1 is not arithmetic."
                        ]
                    },
                    {
                        "metric_name": "Multi-Turn Math",
                        "metric_measures": "Assesses ability to maintain mathematical accuracy across extended problem-solving discussions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better).",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests sustained problem-solving",
                            "Evaluates mathematical guidance",
                            "Assesses error correction",
                            "Measures concept explanation",
                            "Tests progressive difficulty",
                            "Evaluates adaptive teaching"
                        ],
                        "ex_questions": [
                            "Help me solve this calculus problem step by step, explaining each stage of integration by parts.",
                            "Guide me through proving the Pythagorean theorem, addressing my questions at each step.",
                            "Walk me through solving this system of linear equations, explaining alternative approaches."
                        ]
                    },
                    {
                        "metric_name": "Multilingual Maths (MGSM)",
                        "metric_measures": "Evaluates mathematical problem-solving across different languages.",
                        "score_interpretation": "Higher scores indicate better multilingual mathematical capabilities.",
                        "metric_origin": "LMSYS Org, UC Berkeley",
                        "metric_details": [
                            "Tests mathematical reasoning across languages",
                            "Evaluates problem interpretation",
                            "Assesses solution accuracy",
                            "Measures terminology understanding",
                            "Tests cultural context adaptation",
                            "Evaluates consistent methodology"
                        ],
                        "ex_questions": [
                            "Solve this geometry problem presented in both Mandarin and English: Find the area of a triangle with base 6cm and height 8cm.",
                            "Resuelve esta ecuación cuadrática: 2x² + 5x - 3 = 0 (Solve this quadratic equation in Spanish).",
                            "Résoudre ce problème de probabilité (Solve this probability problem in French)."
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
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard includes several mathematics-specific benchmarks.",
                "analysis_tips": [
                    "Higher scores indicate better performance across all metrics.",
                    "Pay attention to both pure mathematical reasoning and applied problem-solving.",
                    "Compare models' performance across different types of mathematical tasks.",
                    "Consider how models perform on both theoretical and practical mathematics."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
                    {
                        "metric_name": "Quantitative Reasoning (MATH)",
                        "metric_measures": "Tests mathematical reasoning and problem-solving skills across various domains.",
                        "score_interpretation": "Higher scores indicate better mathematical reasoning capabilities.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Tests advanced mathematical concepts",
                            "Evaluates problem-solving strategies",
                            "Assesses logical reasoning",
                            "Measures proof comprehension",
                            "Tests abstract thinking",
                            "Evaluates mathematical rigor"
                        ],
                        "ex_questions": [
                            "Prove that the sum of two continuous functions is continuous.",
                            "Solve this optimization problem using Lagrange multipliers.",
                            "Determine the convergence of this infinite series using appropriate tests."
                        ]
                    },
                    {
                        "metric_name": "Scientific Reasoning & Knowledge (GPQA Diamond)",
                        "metric_measures": "Evaluates ability to solve quantitative problems in scientific contexts.",
                        "score_interpretation": "Higher scores indicate better scientific problem-solving ability.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests applied mathematics",
                            "Evaluates physics calculations",
                            "Assesses statistical analysis",
                            "Measures dimensional analysis",
                            "Tests scientific notation",
                            "Evaluates error analysis"
                        ],
                        "ex_questions": [
                            "Calculate the electric field at a point given multiple charged particles.",
                            "Determine the half-life of a radioactive substance from experimental data.",
                            "Solve this chemical equilibrium problem using mathematical principles."
                        ]
                    },
                    {
                        "metric_name": "Multilingual Maths (MGSM)",
                        "metric_measures": "Evaluates mathematical problem-solving across different languages and cultural contexts.",
                        "score_interpretation": "Higher scores indicate better multilingual mathematical capabilities.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests universal mathematical concepts",
                            "Evaluates language-independent reasoning",
                            "Assesses numerical literacy",
                            "Measures problem interpretation",
                            "Tests mathematical communication",
                            "Evaluates cultural context awareness"
                        ],
                        "ex_questions": [
                            "解这个线性方程组 (Solve this system of linear equations in Chinese).",
                            "Calcolare l'integrale definito (Calculate this definite integral in Italian).",
                            "Решите эту задачу оптимизации (Solve this optimization problem in Russian)."
                        ]
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "metrics": [
                    {
                        "metric_name": "MATH Lvl 5",
                        "metric_measures": "Evaluates performance on advanced mathematical problems at a high difficulty level.",
                        "score_interpretation": "Higher scores indicate better advanced mathematical capabilities.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Tests advanced mathematics",
                            "Evaluates complex problem-solving",
                            "Assesses theoretical understanding",
                            "Measures proof construction",
                            "Tests abstract reasoning",
                            "Evaluates mathematical communication"
                        ],
                        "ex_questions": [
                            "Prove that there are infinitely many prime numbers of the form 4n + 1.",
                            "Find all complex solutions to z^4 + 4z^3 + 6z^2 + 4z + 1 = 0.",
                            "Determine the volume of the solid formed by rotating y = sin(x) from 0 to π around the x-axis."
                        ]
                    },
                    {
                        "metric_name": "MATH Lvl 5 Raw",
                        "metric_measures": "Provides unprocessed scores from Level 5 MATH dataset evaluations.",
                        "score_interpretation": "Higher scores reflect better raw performance on advanced mathematics.",
                        "metric_origin": "Hendrycks et al., UC Berkeley",
                        "metric_details": [
                            "Presents unmodified scores",
                            "Shows direct performance data",
                            "Assesses raw accuracy",
                            "Measures unadjusted results",
                            "Tests complete solutions",
                            "Evaluates step-by-step work"
                        ],
                        "ex_questions": [
                            "Solve this differential equation showing all steps: y'' + 4y' + 4y = e^(-2x).",
                            "Prove the Fundamental Theorem of Algebra with detailed reasoning.",
                            "Calculate the exact value of this improper integral: ∫(0 to ∞) x^2e^(-x) dx."
                        ]
                    },
                    {
                        "metric_name": "GSM8K",
                        "metric_measures": "Evaluates ability to solve grade school math word problems.",
                        "score_interpretation": "Higher scores indicate better practical math problem-solving ability.",
                        "metric_origin": "OpenAI Research",
                        "metric_details": [
                            "Tests practical mathematics",
                            "Evaluates word problem comprehension",
                            "Assesses step-by-step reasoning",
                            "Measures arithmetic accuracy",
                            "Tests problem interpretation",
                            "Evaluates solution explanation"
                        ],
                        "ex_questions": [
                            "Tom has 3 times as many marbles as Jane. Jane has 2 more marbles than Sam. If Sam has 4 marbles, how many marbles do they have in total?",
                            "A store offers a 20% discount on a $50 item. If sales tax is 8%, what is the final price?",
                            "If it takes 6 workers 4 days to build a wall, how many days would it take 8 workers to build the same wall?"
                        ]
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
            {
                "leaderboard": "Papers with Code",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/sota/math-word-problem-solving-on-math"
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
                    {
                        "metric_name": "Transcription Accuracy",
                        "metric_measures": "Evaluates overall accuracy of speech recognition across various conditions.",
                        "score_interpretation": "Higher scores indicate better transcription accuracy.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests word accuracy",
                            "Evaluates punctuation placement",
                            "Assesses grammar correction",
                            "Measures speaker differentiation",
                            "Tests context understanding",
                            "Evaluates formatting accuracy"
                        ],
                        "ex_questions": [
                            "Compare transcription accuracy between native and non-native speakers.",
                            "Evaluate punctuation accuracy in complex sentences.",
                            "Assess formatting consistency in different document types."
                        ]
                    },
                    {
                        "metric_name": "Real-World Robustness",
                        "metric_measures": "Assesses performance in challenging real-world conditions.",
                        "score_interpretation": "Higher scores indicate better handling of real-world scenarios.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests background noise handling",
                            "Evaluates accent recognition",
                            "Assesses microphone quality impact",
                            "Measures distance adaptation",
                            "Tests multi-speaker scenarios",
                            "Evaluates environmental resilience"
                        ],
                        "ex_questions": [
                            "Analyze performance in a busy cafe environment.",
                            "Compare accuracy between professional and consumer microphones.",
                            "Evaluate recognition quality at different speaker distances."
                        ]
                    },
                    {
                        "metric_name": "Processing Efficiency",
                        "metric_measures": "Evaluates the speed and resource usage of speech recognition.",
                        "score_interpretation": "Higher scores indicate more efficient processing.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests processing speed",
                            "Evaluates resource usage",
                            "Assesses batch handling",
                            "Measures real-time capability",
                            "Tests memory efficiency",
                            "Evaluates scaling performance"
                        ],
                        "ex_questions": [
                            "Compare processing time for different audio lengths.",
                            "Evaluate performance under different computational constraints.",
                            "Assess real-time transcription capabilities."
                        ]
                    },
                    {
                        "metric_name": "Specialized Content",
                        "metric_measures": "Tests accuracy on domain-specific and technical content.",
                        "score_interpretation": "Higher scores indicate better specialized content handling.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests technical terminology",
                            "Evaluates domain adaptation",
                            "Assesses jargon accuracy",
                            "Measures consistency",
                            "Tests field-specific terms",
                            "Evaluates context understanding"
                        ],
                        "ex_questions": [
                            "Compare accuracy in medical versus legal terminology.",
                            "Evaluate recognition of technical scientific terms.",
                            "Assess performance on industry-specific jargon."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "Common Voice",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/dataset/common-voice"
                },
                "tooltip": "Mozilla's Common Voice is a comprehensive benchmark for evaluating speech recognition across multiple languages and accents.",
                "analysis_tips": [
                    "Lower WER and CER scores indicate better performance.",
                    "Consider performance across different languages if multilingual support is needed.",
                    "Pay attention to both clean and noisy audio performance.",
                    "Look for models tested on diverse speaker demographics."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/1912.06670"
                },
                "metrics": [
                    {
                        "metric_name": "Word Error Rate (WER)",
                        "metric_measures": "Evaluates accuracy of speech recognition by measuring word-level errors.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "Speech Recognition Research",
                        "metric_details": [
                            "Tests word accuracy",
                            "Evaluates word substitutions",
                            "Assesses word deletions",
                            "Measures word insertions",
                            "Tests sentence structure",
                            "Evaluates contextual understanding"
                        ],
                        "ex_questions": [
                            "Compare WER across different accent variations of English.",
                            "Evaluate word accuracy in noisy versus clean audio conditions.",
                            "Assess recognition accuracy for technical terminology."
                        ]
                    },
                    {
                        "metric_name": "Character Error Rate (CER)",
                        "metric_measures": "Assesses transcription accuracy at the character level.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "Speech Recognition Research",
                        "metric_details": [
                            "Tests character-level accuracy",
                            "Evaluates spelling precision",
                            "Assesses phonetic accuracy",
                            "Measures punctuation handling",
                            "Tests diacritic recognition",
                            "Evaluates character substitutions"
                        ],
                        "ex_questions": [
                            "Analyze character-level accuracy in proper nouns.",
                            "Compare performance on languages with different character sets.",
                            "Evaluate accuracy in continuous versus isolated speech."
                        ]
                    },
                    {
                        "metric_name": "Sentence Error Rate (SER)",
                        "metric_measures": "Evaluates the proportion of sentences with any transcription errors.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "Mozilla Common Voice Team",
                        "metric_details": [
                            "Tests sentence-level accuracy",
                            "Evaluates complete utterances",
                            "Assesses semantic preservation",
                            "Measures grammatical correctness",
                            "Tests context preservation",
                            "Evaluates meaning accuracy"
                        ],
                        "ex_questions": [
                            "Compare sentence accuracy across different speaking speeds.",
                            "Evaluate performance on complex versus simple sentences.",
                            "Assess accuracy in conversational versus formal speech."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "LibriSpeech ASR",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean"
                },
                "tooltip": "LibriSpeech is a benchmark derived from audiobooks, offering both clean and noisy speech recognition evaluations.",
                "analysis_tips": [
                    "Consider both test-clean and test-other (noisy) scores.",
                    "Compare performance between read speech and spontaneous speech.",
                    "Look for models that maintain consistency across different speakers.",
                    "Pay attention to real-time factor for production deployment."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/1912.01766"
                },
                "metrics": [
                    {
                        "metric_name": "Clean Speech WER",
                        "metric_measures": "Evaluates word error rate on clear, well-recorded speech samples.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "LibriSpeech Research Team",
                        "metric_details": [
                            "Tests ideal conditions",
                            "Evaluates clear articulation",
                            "Assesses baseline accuracy",
                            "Measures optimal performance",
                            "Tests speaker consistency",
                            "Evaluates pronunciation clarity"
                        ],
                        "ex_questions": [
                            "Compare accuracy between different speaking rates in clean conditions.",
                            "Evaluate performance on professional versus amateur readers.",
                            "Assess recognition of clearly articulated technical terms."
                        ]
                    },
                    {
                        "metric_name": "Noisy Speech WER",
                        "metric_measures": "Assesses word error rate on speech samples with background noise or poor recording quality.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "LibriSpeech Research Team",
                        "metric_details": [
                            "Tests noise resilience",
                            "Evaluates robustness",
                            "Assesses interference handling",
                            "Measures signal separation",
                            "Tests acoustic adaptation",
                            "Evaluates error recovery"
                        ],
                        "ex_questions": [
                            "Analyze performance with different types of background noise.",
                            "Compare accuracy at various signal-to-noise ratios.",
                            "Evaluate recognition in reverberant conditions."
                        ]
                    },
                    {
                        "metric_name": "Real-Time Factor (RTF)",
                        "metric_measures": "Evaluates processing speed relative to audio duration.",
                        "score_interpretation": "Lower values indicate faster processing (RTF < 1 means faster than real-time).",
                        "metric_origin": "LibriSpeech Research Team",
                        "metric_details": [
                            "Tests processing speed",
                            "Evaluates latency",
                            "Assesses computational efficiency",
                            "Measures throughput",
                            "Tests resource usage",
                            "Evaluates batch processing"
                        ],
                        "ex_questions": [
                            "Compare processing speed for different audio lengths.",
                            "Evaluate real-time performance under varying loads.",
                            "Assess latency with different hardware configurations."
                        ]
                    },
                    {
                        "metric_name": "Homophone Accuracy",
                        "metric_measures": "Tests ability to correctly transcribe words that sound identical but have different meanings.",
                        "score_interpretation": "Higher percentages indicate better accuracy (100% is perfect).",
                        "metric_origin": "LibriSpeech Research Team",
                        "metric_details": [
                            "Tests contextual understanding",
                            "Evaluates semantic disambiguation",
                            "Assesses context usage",
                            "Measures word choice",
                            "Tests grammar awareness",
                            "Evaluates meaning preservation"
                        ],
                        "ex_questions": [
                            "Evaluate accuracy in distinguishing 'their/there/they're' based on context.",
                            "Compare performance on technical homophones in different fields.",
                            "Assess contextual disambiguation in continuous speech."
                        ]
                    }
                ]
            },
            # Add to the Speech to text array:
            {
                "leaderboard": "English Speech Benchmark (ESB)",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/dataset/esb"
                },
                "tooltip": "The English Speech Benchmark evaluates speech recognition across diverse accents, speaking styles, and recording conditions.",
                "analysis_tips": [
                    "Consider performance across different English accents.",
                    "Pay attention to scores on spontaneous versus prepared speech.",
                    "Look for models that handle diverse speaking styles well.",
                    "Compare performance on different speech domains (interviews, lectures, conversations)."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2210.13352"
                },
                "metrics": [
                    {
                        "metric_name": "Accent Robustness",
                        "metric_measures": "Evaluates recognition accuracy across different English accents and dialects.",
                        "score_interpretation": "Higher scores indicate better accent handling (0-100).",
                        "metric_origin": "ESB Research Team",
                        "metric_details": [
                            "Tests accent variation",
                            "Evaluates dialect handling",
                            "Assesses pronunciation differences",
                            "Measures regional adaptability",
                            "Tests phonetic variations",
                            "Evaluates accent bias"
                        ],
                        "ex_questions": [
                            "Compare recognition accuracy between British and Indian English accents.",
                            "Evaluate performance on non-native English speakers from different regions.",
                            "Assess adaptation to regional pronunciation patterns."
                        ]
                    },
                    {
                        "metric_name": "Spontaneous Speech WER",
                        "metric_measures": "Assesses accuracy on natural, unscripted speech with disfluencies.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "ESB Research Team",
                        "metric_details": [
                            "Tests natural speech",
                            "Evaluates disfluency handling",
                            "Assesses hesitation markers",
                            "Measures filler word handling",
                            "Tests self-corrections",
                            "Evaluates incomplete utterances"
                        ],
                        "ex_questions": [
                            "Analyze accuracy in handling speech repairs and restarts.",
                            "Compare performance on formal versus casual conversations.",
                            "Evaluate recognition of filler words and hesitations."
                        ]
                    },
                    {
                        "metric_name": "Domain Adaptation Score",
                        "metric_measures": "Evaluates performance across different speech domains and contexts.",
                        "score_interpretation": "Higher scores indicate better domain adaptation (0-100).",
                        "metric_origin": "ESB Research Team",
                        "metric_details": [
                            "Tests domain transfer",
                            "Evaluates context handling",
                            "Assesses vocabulary adaptation",
                            "Measures style transfer",
                            "Tests jargon recognition",
                            "Evaluates register adaptation"
                        ],
                        "ex_questions": [
                            "Compare accuracy between academic lectures and casual conversations.",
                            "Evaluate performance on technical presentations versus interviews.",
                            "Assess recognition of domain-specific terminology."
                        ]
                    },
                    {
                        "metric_name": "Speaking Rate Robustness",
                        "metric_measures": "Tests recognition accuracy across different speaking speeds.",
                        "score_interpretation": "Higher scores indicate better handling of varied speech rates (0-100).",
                        "metric_origin": "ESB Research Team",
                        "metric_details": [
                            "Tests speed variation",
                            "Evaluates rapid speech",
                            "Assesses slow speech",
                            "Measures rhythm handling",
                            "Tests temporal adaptation",
                            "Evaluates pace changes"
                        ],
                        "ex_questions": [
                            "Compare accuracy between fast and slow speakers.",
                            "Evaluate performance on varying speech rates within the same utterance.",
                            "Assess recognition quality during speed transitions."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "SpeechOcean762",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/dataset/speechocean762"
                },
                "tooltip": "SpeechOcean762 is a multilingual benchmark focusing on real-world speech recognition scenarios, including challenging acoustic conditions.",
                "analysis_tips": [
                    "Consider performance across different environmental conditions.",
                    "Pay attention to far-field versus near-field speech recognition.",
                    "Look for models that handle overlapping speech well.",
                    "Compare scores across different microphone types and configurations."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2303.11355"
                },
                "metrics": [
                    {
                        "metric_name": "Environmental Robustness",
                        "metric_measures": "Evaluates recognition accuracy across different acoustic environments.",
                        "score_interpretation": "Higher scores indicate better environmental adaptation (0-100).",
                        "metric_origin": "SpeechOcean Research Team",
                        "metric_details": [
                            "Tests acoustic variations",
                            "Evaluates background noise",
                            "Assesses reverberation handling",
                            "Measures echo cancellation",
                            "Tests ambient adaptation",
                            "Evaluates spatial acoustics"
                        ],
                        "ex_questions": [
                            "Compare recognition accuracy in indoor versus outdoor environments.",
                            "Evaluate performance in rooms with different reverberation characteristics.",
                            "Assess adaptation to varying background noise types."
                        ]
                    },
                    {
                        "metric_name": "Distance Robustness",
                        "metric_measures": "Assesses performance at varying distances between speaker and microphone.",
                        "score_interpretation": "Higher scores indicate better distance handling (0-100).",
                        "metric_origin": "SpeechOcean Research Team",
                        "metric_details": [
                            "Tests far-field speech",
                            "Evaluates volume variation",
                            "Assesses signal strength",
                            "Measures distance impact",
                            "Tests microphone arrays",
                            "Evaluates spatial processing"
                        ],
                        "ex_questions": [
                            "Compare accuracy between close-talking and far-field scenarios.",
                            "Evaluate performance degradation with increasing distance.",
                            "Assess recognition quality with different microphone configurations."
                        ]
                    },
                    {
                        "metric_name": "Overlapping Speech Accuracy",
                        "metric_measures": "Tests ability to recognize speech in multi-speaker scenarios.",
                        "score_interpretation": "Higher scores indicate better handling of overlapping speech (0-100).",
                        "metric_origin": "SpeechOcean Research Team",
                        "metric_details": [
                            "Tests speaker separation",
                            "Evaluates voice disambiguation",
                            "Assesses cross-talk handling",
                            "Measures speaker tracking",
                            "Tests conversation flow",
                            "Evaluates interference rejection"
                        ],
                        "ex_questions": [
                            "Analyze accuracy in transcribing overlapping conversations.",
                            "Compare performance with different numbers of simultaneous speakers.",
                            "Evaluate speaker attribution in mixed conversations."
                        ]
                    },
                    {
                        "metric_name": "Device Adaptation",
                        "metric_measures": "Evaluates performance across different recording devices and microphone types.",
                        "score_interpretation": "Higher scores indicate better device adaptability (0-100).",
                        "metric_origin": "SpeechOcean Research Team",
                        "metric_details": [
                            "Tests device variation",
                            "Evaluates microphone quality",
                            "Assesses hardware differences",
                            "Measures frequency response",
                            "Tests sampling rates",
                            "Evaluates signal processing"
                        ],
                        "ex_questions": [
                            "Compare recognition quality between professional and consumer microphones.",
                            "Evaluate performance across different mobile device types.",
                            "Assess adaptation to varying audio sampling rates."
                        ]
                    }
                ]
            }
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
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "metrics": [
                    {
                        "metric_name": "Voice Naturalness",
                        "metric_measures": "Evaluates how natural and human-like the synthesized speech sounds.",
                        "score_interpretation": "Higher scores indicate more natural-sounding speech.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests human-likeness",
                            "Evaluates prosody quality",
                            "Assesses voice consistency",
                            "Measures emotional expression",
                            "Tests accent authenticity",
                            "Evaluates speaking rhythm"
                        ],
                        "ex_questions": [
                            "Compare naturalness between emotional and neutral speech synthesis.",
                            "Evaluate prosody in questions versus statements.",
                            "Assess the authenticity of different speaking styles."
                        ]
                    },
                    {
                        "metric_name": "Voice Clarity",
                        "metric_measures": "Assesses the clarity and intelligibility of synthesized speech.",
                        "score_interpretation": "Higher scores indicate clearer speech output.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests pronunciation clarity",
                            "Evaluates articulation",
                            "Assesses audio quality",
                            "Measures word boundaries",
                            "Tests phoneme accuracy",
                            "Evaluates speaker consistency"
                        ],
                        "ex_questions": [
                            "Compare clarity in fast versus normal speech rates.",
                            "Evaluate pronunciation of technical terms.",
                            "Assess intelligibility in different acoustic contexts."
                        ]
                    },
                    {
                        "metric_name": "Processing Speed",
                        "metric_measures": "Evaluates the time taken to generate speech from text input.",
                        "score_interpretation": "Higher scores indicate faster processing.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests generation speed",
                            "Evaluates latency",
                            "Assesses real-time capability",
                            "Measures throughput",
                            "Tests batch processing",
                            "Evaluates resource efficiency"
                        ],
                        "ex_questions": [
                            "Compare processing speed for different text lengths.",
                            "Evaluate real-time performance under varying loads.",
                            "Assess scalability with batch processing."
                        ]
                    },
                    {
                        "metric_name": "Speaker Consistency",
                        "metric_measures": "Evaluates the model's ability to maintain consistent voice characteristics.",
                        "score_interpretation": "Higher scores indicate better consistency.",
                        "metric_origin": "Artificial Analysis Research Team",
                        "metric_details": [
                            "Tests voice stability",
                            "Evaluates accent maintenance",
                            "Assesses style preservation",
                            "Measures tonal consistency",
                            "Tests character retention",
                            "Evaluates speaker identity"
                        ],
                        "ex_questions": [
                            "Compare voice consistency across long passages.",
                            "Evaluate maintenance of speaking style in different contexts.",
                            "Assess stability of voice characteristics over time."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "Papers with Code TTS",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/task/text-to-speech-synthesis"
                },
                "tooltip": "Papers with Code maintains a comprehensive leaderboard for text-to-speech synthesis across various benchmarks and datasets.",
                "analysis_tips": [
                    "Lower MOS (Mean Opinion Score) and WER (Word Error Rate) scores indicate better performance.",
                    "Consider both objective metrics and subjective human evaluations.",
                    "Pay attention to the specific dataset used for each evaluation.",
                    "Look for models tested on multiple languages if multilingual support is needed."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://paperswithcode.com/methods/category/text-to-speech-synthesis"
                },
                "metrics": [
                    {
                        "metric_name": "Mean Opinion Score (MOS)",
                        "metric_measures": "Evaluates perceived naturalness and quality of synthesized speech through human ratings.",
                        "score_interpretation": "Scores range from 1-5 (higher is better).",
                        "metric_origin": "ITU-T Recommendation P.800",
                        "metric_details": [
                            "Tests overall speech quality",
                            "Evaluates naturalness",
                            "Assesses voice clarity",
                            "Measures pronunciation accuracy",
                            "Tests speaker similarity",
                            "Evaluates prosody quality"
                        ],
                        "ex_questions": [
                            "Rate the naturalness of this synthesized voice passage.",
                            "Compare the quality of emotional expression in these two speech samples.",
                            "Evaluate how well this voice matches the target speaker."
                        ]
                    },
                    {
                        "metric_name": "Word Error Rate (WER)",
                        "metric_measures": "Assesses accuracy of speech synthesis by measuring word-level errors.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "Speech Recognition Research",
                        "metric_details": [
                            "Tests word accuracy",
                            "Evaluates pronunciation errors",
                            "Assesses word insertions",
                            "Measures word deletions",
                            "Tests word substitutions",
                            "Evaluates sequence accuracy"
                        ],
                        "ex_questions": [
                            "Compare the transcribed text with the original input to identify errors.",
                            "Analyze pronunciation accuracy in technical terms and proper nouns.",
                            "Evaluate word sequence preservation in long sentences."
                        ]
                    },
                    {
                        "metric_name": "Character Error Rate (CER)",
                        "metric_measures": "Evaluates accuracy at the character level rather than word level.",
                        "score_interpretation": "Lower percentages indicate better accuracy (0% is perfect).",
                        "metric_origin": "Speech Recognition Research",
                        "metric_details": [
                            "Tests character accuracy",
                            "Evaluates phoneme correctness",
                            "Assesses character insertions",
                            "Measures character deletions",
                            "Tests character substitutions",
                            "Evaluates pronunciation details"
                        ],
                        "ex_questions": [
                            "Analyze character-level accuracy in complex proper nouns.",
                            "Compare phoneme accuracy between different accent variations.",
                            "Evaluate detailed pronunciation in multilingual text."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "ASR Research Leaderboard",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean"
                },
                "tooltip": "While primarily focused on speech recognition, the ASR leaderboard includes crucial metrics for evaluating text-to-speech quality through recognition accuracy.",
                "analysis_tips": [
                    "Lower PESQ and STOI scores indicate better speech quality.",
                    "Consider real-time factor (RTF) for production deployment.",
                    "Pay attention to performance across different speaking rates.",
                    "Look for models tested in noisy conditions if robustness is important."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2303.01037"
                },
                "metrics": [
                    {
                        "metric_name": "PESQ (Perceptual Evaluation of Speech Quality)",
                        "metric_measures": "Evaluates the quality of synthesized speech using an ITU standard for audio quality assessment.",
                        "score_interpretation": "Scores range from -0.5 to 4.5 (higher is better).",
                        "metric_origin": "ITU-T P.862",
                        "metric_details": [
                            "Tests perceptual quality",
                            "Evaluates audio distortion",
                            "Assesses noise levels",
                            "Measures frequency response",
                            "Tests temporal degradation",
                            "Evaluates artifact presence"
                        ],
                        "ex_questions": [
                            "Compare the PESQ scores between clear and noisy conditions.",
                            "Evaluate the quality degradation in different bandwidth conditions.",
                            "Assess the impact of compression on speech quality."
                        ]
                    },
                    {
                        "metric_name": "STOI (Short-Time Objective Intelligibility)",
                        "metric_measures": "Assesses the intelligibility of synthesized speech through objective measurements.",
                        "score_interpretation": "Scores range from 0 to 1 (higher is better).",
                        "metric_origin": "Technical University of Denmark",
                        "metric_details": [
                            "Tests speech intelligibility",
                            "Evaluates temporal patterns",
                            "Assesses spectral clarity",
                            "Measures phonetic preservation",
                            "Tests modulation accuracy",
                            "Evaluates speech coherence"
                        ],
                        "ex_questions": [
                            "Analyze intelligibility preservation in fast speech synthesis.",
                            "Compare STOI scores across different speaker styles.",
                            "Evaluate intelligibility in challenging acoustic conditions."
                        ]
                    },
                    {
                        "metric_name": "Real-Time Factor (RTF)",
                        "metric_measures": "Evaluates the speed of speech synthesis relative to the duration of generated audio.",
                        "score_interpretation": "Lower values indicate faster synthesis (RTF < 1 means faster than real-time).",
                        "metric_origin": "Speech Synthesis Research",
                        "metric_details": [
                            "Tests processing speed",
                            "Evaluates computational efficiency",
                            "Assesses latency",
                            "Measures throughput",
                            "Tests resource usage",
                            "Evaluates scalability"
                        ],
                        "ex_questions": [
                            "Calculate RTF for generating a 10-minute speech sample.",
                            "Compare synthesis speed across different model sizes.",
                            "Evaluate real-time performance under varying loads."
                        ]
                    },
                    {
                        "metric_name": "F0 RMSE",
                        "metric_measures": "Measures accuracy of fundamental frequency (pitch) reproduction in synthesized speech.",
                        "score_interpretation": "Lower values indicate better pitch accuracy (0 is perfect).",
                        "metric_origin": "Speech Synthesis Research",
                        "metric_details": [
                            "Tests pitch accuracy",
                            "Evaluates intonation patterns",
                            "Assesses prosody matching",
                            "Measures pitch range",
                            "Tests pitch stability",
                            "Evaluates stress patterns"
                        ],
                        "ex_questions": [
                            "Compare pitch accuracy between emotional and neutral speech.",
                            "Evaluate intonation preservation in questions versus statements.",
                            "Assess pitch variation in expressive speech synthesis."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "LJSpeech Benchmark",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://paperswithcode.com/sota/text-to-speech-synthesis-on-ljspeech"
                },
                "tooltip": "LJSpeech is a widely-used benchmark for evaluating English text-to-speech systems, focusing on single-speaker synthesis quality.",
                "analysis_tips": [
                    "Compare MOS scores across different speaking styles.",
                    "Consider both objective metrics and subjective listener ratings.",
                    "Pay attention to prosody and naturalness scores.",
                    "Look for models that maintain quality across longer utterances."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/1905.08459"
                },
                "metrics": [
                    {
                        "metric_name": "Mel Cepstral Distortion (MCD)",
                        "metric_measures": "Evaluates the spectral distance between synthesized and reference speech.",
                        "score_interpretation": "Lower values indicate better quality (measured in dB).",
                        "metric_origin": "Speech Synthesis Research Community",
                        "metric_details": [
                            "Tests spectral accuracy",
                            "Evaluates acoustic similarity",
                            "Assesses voice characteristics",
                            "Measures timbre accuracy",
                            "Tests frequency response",
                            "Evaluates spectral envelope"
                        ],
                        "ex_questions": [
                            "Compare MCD scores between fast and normal speech synthesis.",
                            "Evaluate spectral accuracy in different frequency ranges.",
                            "Assess voice characteristic preservation across utterances."
                        ]
                    },
                    {
                        "metric_name": "Prosody L2 Error",
                        "metric_measures": "Assesses accuracy of rhythm, stress, and intonation patterns.",
                        "score_interpretation": "Lower values indicate better prosodic accuracy (0 is perfect).",
                        "metric_origin": "LJSpeech Research Team",
                        "metric_details": [
                            "Tests rhythm accuracy",
                            "Evaluates stress patterns",
                            "Assesses intonation curves",
                            "Measures pause timing",
                            "Tests emphasis accuracy",
                            "Evaluates speaking rate"
                        ],
                        "ex_questions": [
                            "Analyze prosodic accuracy in emotional speech synthesis.",
                            "Compare stress patterns between synthesized and natural speech.",
                            "Evaluate the timing of pauses in long sentences."
                        ]
                    },
                    {
                        "metric_name": "Voice Consistency Score",
                        "metric_measures": "Evaluates consistency of voice characteristics across different utterances.",
                        "score_interpretation": "Higher scores indicate better consistency (0-100).",
                        "metric_origin": "LJSpeech Research Team",
                        "metric_details": [
                            "Tests speaker identity",
                            "Evaluates voice stability",
                            "Assesses timbre consistency",
                            "Measures style preservation",
                            "Tests acoustic coherence",
                            "Evaluates character maintenance"
                        ],
                        "ex_questions": [
                            "Compare voice consistency across different sentence lengths.",
                            "Evaluate speaker identity preservation in varying emotional contexts.",
                            "Assess timbre stability across different phonetic contexts."
                        ]
                    },
                    {
                        "metric_name": "Naturalness MOS",
                        "metric_measures": "Specific Mean Opinion Score focusing on speech naturalness.",
                        "score_interpretation": "Scores range from 1-5 (higher is better).",
                        "metric_origin": "LJSpeech Research Team",
                        "metric_details": [
                            "Tests human-likeness",
                            "Evaluates natural flow",
                            "Assesses pronunciation",
                            "Measures fluency",
                            "Tests natural timing",
                            "Evaluates expression quality"
                        ],
                        "ex_questions": [
                            "Rate the naturalness of conversational speech synthesis.",
                            "Compare naturalness between different speaking styles.",
                            "Evaluate the human-likeness of emotional expressions."
                        ]
                    }
                ]
            },
            {
                "leaderboard": "Nvidia NeMo Framework",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://catalog.ngc.nvidia.com/models?filters=&orderBy=weightPopularDESC&query=nemo-tts"
                },
                "tooltip": "Nvidia's NeMo framework provides standardized benchmarks for evaluating text-to-speech models, with particular focus on production-ready metrics.",
                "analysis_tips": [
                    "Consider both quality and speed metrics for production deployment.",
                    "Pay attention to multi-speaker adaptation scores if relevant.",
                    "Look at performance across different speech durations.",
                    "Compare resource requirements alongside quality metrics."
                ],
                "paper": {
                    "text": "Nerdy details 🤓",
                    "url": "https://arxiv.org/abs/2104.05557"
                },
                "metrics": [
                    {
                        "metric_name": "Multi-Speaker Similarity",
                        "metric_measures": "Evaluates how well the model adapts to and maintains different speaker identities.",
                        "score_interpretation": "Higher scores indicate better speaker adaptation (0-100).",
                        "metric_origin": "Nvidia Research",
                        "metric_details": [
                            "Tests speaker adaptation",
                            "Evaluates voice cloning accuracy",
                            "Assesses identity preservation",
                            "Measures cross-speaker consistency",
                            "Tests accent preservation",
                            "Evaluates style transfer"
                        ],
                        "ex_questions": [
                            "Compare voice similarity scores across different speaker demographics.",
                            "Evaluate accent preservation in multi-speaker synthesis.",
                            "Assess identity maintenance across different speaking styles."
                        ]
                    },
                    {
                        "metric_name": "FastPitch Score",
                        "metric_measures": "Assesses the model's ability to control speech rhythm and pitch accurately.",
                        "score_interpretation": "Lower scores indicate better pitch and rhythm control (0 is perfect).",
                        "metric_origin": "Nvidia Research",
                        "metric_details": [
                            "Tests pitch accuracy",
                            "Evaluates rhythm control",
                            "Assesses duration modeling",
                            "Measures energy control",
                            "Tests prosody transfer",
                            "Evaluates style preservation"
                        ],
                        "ex_questions": [
                            "Analyze pitch accuracy in expressive speech synthesis.",
                            "Compare rhythm control in different languages.",
                            "Evaluate energy contour preservation in emotional speech."
                        ]
                    },
                    {
                        "metric_name": "Inference Latency",
                        "metric_measures": "Evaluates the speed of speech generation in a production environment.",
                        "score_interpretation": "Lower values indicate faster generation (measured in milliseconds).",
                        "metric_origin": "Nvidia Research",
                        "metric_details": [
                            "Tests generation speed",
                            "Evaluates batch processing",
                            "Assesses GPU utilization",
                            "Measures memory usage",
                            "Tests throughput capacity",
                            "Evaluates scaling efficiency"
                        ],
                        "ex_questions": [
                            "Measure generation time for different text lengths.",
                            "Compare latency across different hardware configurations.",
                            "Evaluate performance under varying batch sizes."
                        ]
                    },
                    {
                        "metric_name": "Cross-Language Quality",
                        "metric_measures": "Assesses speech quality across different languages and accents.",
                        "score_interpretation": "Higher scores indicate better multilingual capability (0-100).",
                        "metric_origin": "Nvidia Research",
                        "metric_details": [
                            "Tests language adaptation",
                            "Evaluates accent handling",
                            "Assesses phoneme accuracy",
                            "Measures pronunciation quality",
                            "Tests language switching",
                            "Evaluates cultural markers"
                        ],
                        "ex_questions": [
                            "Compare quality scores across different language families.",
                            "Evaluate code-switching performance in multilingual text.",
                            "Assess pronunciation accuracy in non-native accents."
                        ]
                    }
                ]
            }
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
