# ========================================================================
#   Questions and Recommendation
# ========================================================================


# Question flow structure
QUESTIONS = {
    "task": {
        "question": "What do you want the model to do?",
        "tooltip": "This list isn't exhaustive of what AI can do; it's more representative of the types of tasks that have associated intelligence-leaning performance benchmarks.",
        "options": [
            "Chain agents",
            "Chat",
            "Convert speech to text",
            "Convert text to speech"
            "Generate code",
            "Generate images",
            "Generate text",
            "Generate video",
            "Solve complex problems",
            "Solve math problems",
        ],
        "next": "goal"
    },
    "goal": {
        "question": "What do you want to evaluate?",
        "tooltip": "There are many benchmarks leaderboards provide. The answer to this question will help whittle down the list of benchmarks to choose from.",
        "options": [
            "Quality",
            "Cost",
            "Speed",
            "Latency",
            "Context window"
        ],
        "next": "recommendation"
    }
}

# Original recommendations data structure
RECOMMENDATIONS = {
    "Chain agents": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quality Index",
                        "benchmark_measures": "Evaluates the model's overall ability across reasoning, instruction-following, text generation, and domain-specific tasks such as math and coding.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "QUAKE",
                        "benchmark_measures": "Evaluates practical, multi-step problem-solving, which is fundamental for chain agents orchestrating tasks across different tools.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "SEAL",
                "leaderboard_abbrev": "SEAL",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://scale.com/leaderboard/tool_use"
                },
                "tooltip": "They break up ToolComp into two subsets: ToolComp-Enterprise, which tests usage of 11 tools, and ToolComp-Chat, which tests usage of 2 common chatbot tools (Python Interpreter and Google Search).",
                "analysis_tips": [
                    "Their introduction includes a handy table that compares the tasks included in their benchmark (ToolComp) to other benchmarks.",
                    "In their Data Sample section they include example tasks each model was evaluated on, e.g., 'Calculate the average daytime temperature in Paris during the week of Halloween (October 29th to November 4th, 2023).' They provide 5 examples you can toggle through.",
                    "If you want to gain a better understanding of how agents work under the hood, I highly recommend reading the pseudo-code the models generate. Search for 'thought:' in the Data Sample section.",
                    "In the Prompt Creation section, they categorize the prompts. This is really useful because if your app is going to be used in a vertical not as well represented (e.g., Architecture or Geology), you may want to discount the usefulness of this leaderboard."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://scale.com/leaderboard/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Score",
                        "benchmark_measures": "Score calculates the mean of ToolComp-Enterprise and ToolComp-Chat. ToolComp-Enterprise assesses models on tasks requiring the use of 11 distinct tools, reflecting complex scenarios typical in enterprise settings. ToolComp-Chat evaluates models on tasks involving two common tools\u2014Google Search and Python Interpreter\u2014focusing on general-purpose chatbot capabilities.",
                        "score_interpretation": "Score ranges from 1 to 100 (higher is better)."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/speech-to-text/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Chat": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Communication (LMSys Chatbot Arena ELO Score)",
                        "benchmark_measures": "Evaluates the model's performance in conversational settings, evaluating communication skills, coherence, and engagement based on user feedback.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_abbrev": "Chatbot Arena",
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
                    "Large Model Systems (LMSYS) renamed their 'Elo rating' column to 'Arena Score' in June 2024. Nothing changed but the label (source: https://lmsys.org/blog/2024-06-27-multimodal/)."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2403.04132"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Instruction Following",
                        "benchmark_measures": "Evaluates how well the model follows explicit user instructions.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Multi-Turn",
                        "benchmark_measures": "Evaluates model's performance in multi-turn conversations, reflecting conversational consistency and coherence.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Longer Query",
                        "benchmark_measures": "Evaluates the model's effectiveness in handling and responding accurately to longer, more complex queries.",
                        "score_interpretation": "Score ranges from 1 to the number of models (lower is better)."
                    },
                    {
                        "benchmark_name": "Arena Score",
                        "benchmark_measures": "Ranks models based on performance in head-to-head comparisons. This score is derived using the Elo rating system, a method traditionally employed in chess and other competitive games to assess the relative skill levels of players.",
                        "score_interpretation": "Score ranges from 1 - thousands (higher is better)."
                    }
                ]
            },
            {
                "leaderboard": "FACTS Grounding Leaderboard",
                "leaderboard_abbrev": "FACTS",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.kaggle.com/facts-leaderboard/leaderboard"
                },
                "tooltip": "FACTS is a novel benchmark from Google DeepMind and Google Research designed to evaluate the factual accuracy and grounding of AI models.",
                "analysis_tips": [
                    "Each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request.",
                    "A response is labeled accurate if all its claims are directly supported or don't require support from the context; otherwise, it's marked inaccurate.",
                    'The eval tool uses automated LLM judge models for evaluation. In an effort to make scoring as fair as possible, they use a "range of frontier LLMs" and average the score outputs.',
                    "Where you might thinking clicking on the Factuality Score column heading would sort the column, it actually is a jump link to 'Step 4: Ensembling' lower on the page...which is unusual. That section discusses how Factuality is calculated, so I can kind of understand what they were thinking, but it's still a bit jarring from a usability standpoint.",
                    "I personally love any time a leaderboard includes a knowledge cutoff date. But since most of these models have gone agentic, it's not as essential as it used to be as they frequently search the web for answers and synthesize that information into their responses.",
                    "The full FACTS Grounding benchmark is comprised of 1,719 examples. This includes 860 public examples available in the FACTS Grounding Public Examples Dataset. The remaining 859 examples comprise a private set that will be held out to mitigate risks of benchmark contamination (i.e., model creators cheating by training their models on the test questions to boost their scores).",
                    "There are charts below the leaderboard that show the distribution of tasks (e.g., fact finding, summarizing, concept comparison, etc.) and domains (e.g., medical, legal, etc.).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Factuality",
                        "benchmark_measures": "Evaluates ability to generate factually accurate responses in information-seeking scenarios.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_abbrev": "Hugging Face",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face leaderboard only includes open models, so you won't find performance metrics for proprietary models here (e.g., OpenAI, Google, Anthropic, etc).",
                "analysis_tips": [
                    "You have more viewing options if you select 'table option' above the table.",
                    "I recommend filtering by just chat models. You can do this by selecting the Advanced Filters button in the search field and selecting 'Chat' from Model Type. You have other filter options as well, like model size (measured in parameters), as well as flags.",
                    "If you're building a chatbot for a more technical domain, such as medicine, law, engineering, or math, I'd also look at the MMLU-PRO benchmark."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "IFEval",
                        "benchmark_measures": "Evaluates model's ability to follow explicit formatting instructions.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "All 'tokens per second' metrics refer to OpenAI tokens. At the time of writing the Artificial Analysis team uses OpenAI tokens as a standard unit of measurement across all of its tests to allow fair comparisons between models.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TTFT)",
                        "benchmark_measures": "Time to First Token (TTFT) measures the amount of time it takes for a language model to generate and return the very first token of its response after receiving a user prompt, essentially measuring how quickly a user starts seeing output from the model after initiating a query.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Solve complex problems": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Scientific Reasoning & Knowledge (GPQA Diamond) ",
                        "benchmark_measures": "Evaluates graduate-level reasoning and problem-solving.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_abbrev": "Chatbot Arena",
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
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    },
                    {
                        "benchmark_name": "Multi-Turn Reasoning",
                        "benchmark_measures": "Evaluates ability to maintain logical consistency across extended reasoning chains.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    },
                    {
                        "benchmark_name": "Complex Problem Solving",
                        "benchmark_measures": "Evaluates ability to solve problems requiring multiple steps and consideration of various factors.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_abbrev": "Hugging Face",
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
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "QUAKE",
                        "benchmark_measures": "Evaluates challenging, multi-step problem-solving.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Reasoning",
                        "benchmark_measures": "What Vellum simplifies to 'Reasoning' is actually the Graduate-Level Google-Proof Question Answering (GPQA) benchmark. It is a challenging dataset designed to evaluate the capabilities of LLMs and scalable oversight mechanisms. It comprises 448 multiple-choice questions meticulously crafted by domain experts in biology, physics, and chemistry. These questions are intentionally designed to be high-quality and extremely difficult, ensuring that even experts who have or are pursuing PhDs in the corresponding domains achieve only 65 pct accuracy. The questions are also 'Google-proof', meaning that highly skilled non-expert validators, despite having unrestricted access to the web and spending over 30 minutes per question, only reach 34 pct accuracy. State-of-the-art AI systems, including GPT-4 based models, achieve around 39 pct accuracy on this dataset. The difficulty of GPQA for both skilled non-experts and advanced AI systems makes it an excellent resource for conducting realistic scalable oversight experiments, aiming to explore ways for human experts to reliably obtain truthful information from AI systems that surpass human capabilities.",
                        "score_interpretation": "Scores range from 0-100 pct (higher is better), with a score of 65 pct or greater being classified as equivalent to a human expert."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Generate code": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The only chart relevant to coding in their 'Quality Evaluations' section is 'Coding (HumanEval)' (at the time of writing).",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Coding (HumanEval)",
                        "benchmark_measures": "Evaluates the model's ability to generate syntactically correct and functional code based on problem statements.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "BigCodeBench Leaderboard",
                "leaderboard_abbrev": "BigCodeBench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://bigcode-bench.github.io/"
                },
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2406.15877"
                },
                "analysis_tips": [
                    "This leaderboard is a thick-and-chewy cookie, but I'll break it down as much as possible.",
                    "Pass@1 vs Calibrated Pass@k...What the heck? Okay Pass@1 calculates the percentage of times the model completed the coding task on the first attempt like some kinda showoff. Calibrated Pass@k calculates the percentage of times the model completed the task within the top k attempts. You know...like actual humans. Basically, Pass@k is designed to provide a fairer measurement by considering the model's intent and coding capabilities, even when the output is incomplete or imperfect. The leaderboard uses calibrated Pass@1.",
                    "Now Complete vs Instruct vs Average: Complete evaluates code completion based on detailed docstrings, testing a model's coding proficiency. Instruct assesses code generation from brief natural language instructions, examining a model's ability to understand human intent. So a Complete task might ask a model to complete the function 'def calculate_area(length, width'):' using the provided docstring while an instruct task might prompt might just prompt it to write a Python function to calculate the area of a rectangle. Average represents the mean (aka average)of a model's performance across both the Complete and Instruct tasks.",
                    "If you select the Average filter, you'll see what looks like a dot plot with the average node being the darker dot. If you have multiple models with the same number of parameters they'll line up along the same point on the vertical axis (e.g.,like Llama 3.1-70B-Instruct and Athene-70B).",
                    "Base vs Instructed: With Base, you give the model an instruction like write an API call for a weather API that returns the temperature for NYC. Now let's say you provide it with examples of how you want it to be structured, the export format (csv instead of json), and how you want to handle errors. That's Instructed.",
                    "This toggle may seem buggy, but it's actually pretty intuitive. If all the models disappear, just keep clicking...just keep clicking...What do we like to d\u2014. Just kidding. You need to make sure you don't have the Instruct filter active while having base models (green) selected because, by definition, base models aren't instructed. Complete and Average will show both.",
                    "Show Models with Unknown Sizes: Enables or disables the inclusion of models whose parameter sizes or details are not disclosed. Useful for filtering out incomplete data.",
                    "Base vs Instructed: Base evaluates the model's performance in its default, pre-trained state, without fine-tuning for specific instructions. Instructed evaluates a model fine-tuned or trained to follow natural language instructions. The color coding distinguishes between 'base' models (green) and 'instructed' models (gray), highlighting whether the model has undergone fine-tuning or instruction-based training.",
                    "Show Models with Unknown Size: I don't recommend toggling this on. It's a hot mess.",
                    "Emoji gude: \u2728 marks models evaluated using a chat setting; \ud83d\udca4 indicates the models having at least a difference of 1 pct between the Pass@1 and Calibrated Pass@k; \ud83d\udc9a means open weights and open data, \ud83d\udc99 means open weights and open SFT data (Supervised Fine-Tuning = training a model using a dataset of input-output pairs), but the base model is not data-open. \ud83d\udc9a\ud83d\udc99 models open-source the data."
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Calibrated Pass@1",
                        "benchmark_measures": "Adjusts the raw Pass@1 metric by accounting for common omissions or minor errors in code, such as missing imports or boilerplate. It measures the likelihood of a model generating code that solves a task correctly with slight, acceptable deviations. This is what is shown on the leaderboard.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Pass@1 (Raw)",
                        "benchmark_measures": "The percentage of tasks solved correctly by the first attempt, without calibration for omissions or partial correctness.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_abbrev": "Chatbot Arena",
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
                        "benchmark_measures": "Evaluates the model's ability to understand and generate code effectively.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    }
                ]
            },
            {
                "leaderboard": "CodeXGLUE Leaderboard",
                "leaderboard_abbrev": "CodeXGLUE",
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
                    "The leaderboard is divided into different tasks: clone detection, defect detection, cloze test, code completion, code refinement, code translation, type prediction, natural language code search, code generation, code summarization, and documentation translation. Because Microsoft, amirite? Check which specific task is most relevant to your needs.",
                    "Because the guidelines for submitting models are so stringent and the datasets often require significant preprocessing, not many models participate so keep that in mind when considering this leaderboard.",
                    "One advantage to CodeXGLUE is it's more representative of programming languages besides Python.",
                    "If a column is cut off, hover over a column border and drag it to the left to make room for the obstructed column."
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Overall",
                        "benchmark_measures": "Aggregates performance across all CodeXGLUE tasks to evaluate general code intelligence capabilities",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Clone Detection (Code-Code)",
                        "benchmark_measures": "Identifies semantically equivalent code snippets despite syntactic differences",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Defect Detection (Code-Code)",
                        "benchmark_measures": "Evaluates ability to identify bugs and potential defects in code",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Cloze Test (Code-Code)",
                        "benchmark_measures": "Evaluates understanding of code context by predicting masked tokens in code sequences",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Code Completion (Code-Code)",
                        "benchmark_measures": "Evaluates ability to autocomplete partial code snippets with contextually appropriate suggestions",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Code Refinement (Code-Code)",
                        "benchmark_measures": "Evaluates capacity to improve code quality through bug fixes and optimizations",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Code Translation (Code-Code)",
                        "benchmark_measures": "Evaluates ability to convert code between different programming languages while preserving functionality",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Type Prediction (Code-Code)",
                        "benchmark_measures": "Predicts variable and function types in dynamically typed languages",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Natural Language Code Search (Text-Code)",
                        "benchmark_measures": "Evaluates effectiveness in finding relevant code snippets based on natural language queries",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Code Generation (Text-Code)",
                        "benchmark_measures": "Evaluates ability to create executable code from natural language descriptions",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Code Summarization (Code-Text)",
                        "benchmark_measures": "Evaluates capacity to generate concise natural language descriptions of code functionality",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Documentation Translation (Text-Text)",
                        "benchmark_measures": "Evaluates accuracy in translating technical documentation between different human languages",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "LiveCodeBench",
                "leaderboard_abbrev": "LiveCodeBench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://livecodebench.github.io/leaderboard.html"
                },
                "tooltip": "LiveCodeBench evaluates models on various coding tasks, including code generation, self-repair, code execution, and test output prediction. It collects new problems over time from coding competition platforms like LeetCode, AtCoder, and CodeForces, in an attempt to prevent contamination.",
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2403.07974"
                },
                "analysis_tips": [
                    "At the time of writing SWE-Bench only tests models on Python code.",
                    "The leaderboard provides a slider that allows you to filter by start and end date. You can use this slider to focus on specific periods. Moving the start and end dates changes which coding problems are included in the scores. For example, setting March-April 2024 only shows how models performed on problems published in those months. The number in the first paragraph will dynamically update to show the number of problems in the selected range.",
                    "Models highlighted in red are flagged for data contamination (i.e., evidence of exposure to problems before testing), meaning there is suspicion they may have been exposed to the evaluation problems during training. This is determined by checking if the model's training data overlaps with the time the problems were publicly released or its solutions have unusually high accuracy or training artifacts to identify exact or near-duplicate solutions. These models are not assigned ranks. Think of it like LiveCodeBench's Hall of Shame. 🧐",
                    "To check for contamination yourself, look at how models perform on problems published before their release. If a model has unusually high scores on problems that were public during its training period, it will be highlighted in red. This suggests the model may have been exposed to those problems or solutions during training. Imo, this slider would be more usesful if the leaderboard explicitly included the date the model was evaluated, like many of the other leaderboards.",          
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Pass@1",
                        "benchmark_measures": "Evaluates the percentage of tasks where the model produces a correct solution on the first attempt.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Easy-Pass@1",
                        "benchmark_measures": "Evaluates the percentage of correctly solved 'easy' tasks on the first attempt.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Medium-Pass@1",
                        "benchmark_measures": "Evaluates the percentage of correct solutions for 'medium' difficulty tasks on the first attempt.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Hard-Pass@1",
                        "benchmark_measures": "Evaluates the percentage of correct solutions for 'hard' difficulty tasks on the first attempt.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "SWE-bench",
                "leaderboard_abbrev": "SWE-bench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.swebench.com/"
                },
                "tooltip": "The SWE-bench leaderboard assesses how well language models can resolve real-world software issues sourced from GitHub. For each sample in SWE-bench, agents are provided with the original text from the GitHub issue, known as the problem statement, and are given access to the codebase. Given these, agents must edit the files in the codebase to resolve the issue.",
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2310.06770"
                },
                "analysis_tips": [
                    "The leaderboard has Lite and Verified alternatives. The Lite leaderboard features a subset of SWE-bench that's been curated to make evaluation less costly and more accessible, and the Verified leaderboard features a human annotator-filtered subset that has been deemed to have a ceiling of 100 pct resolution rate.",
                    "At time of writing SWE-Bench only tests models on Python code.",
                    "The benchmark involves giving agents a code repository and issue description, and challenging them to generate a patch that resolves the problem described by the issue.",
                    "The leaderboard uses emojis to indicate status, e.g., models they checked for reproducibility, models with open-source code, etc. The legend is below the leaderboard.",
                    "The leaderboard is updated once a week on Mondays.",
                    "The % Resolved metric refers to the percentage of SWE-bench instances (2294 for test, 500 for verified, 300 for lite) that were resolved by the model.",
                    "The Logs column indicates whether detailed logs of the model's task resolution are available for analysis.",
                    "The Trajs column Indicates whether task execution trajectories are provided for deeper insights into the model's resolution process (i.e., if step-by-step details of how the model solved tasks are available for review).",
                    "Columns can't be sorted.",
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "% Resolved",
                        "benchmark_measures": "Evaluates the percentage of tasks or issues successfully resolved by the model.",
                        "score_interpretation": "Higher is better."
                    },
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
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
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'.",
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Python coding",
                        "benchmark_measures": "Evaluates the model's ability to generate correct Python code from problem statements.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The Artificial Analysis and Vellum leaderboards both use the HumanEval benchmark where KLU uses the BigCodeBench benchmark.",
                    "All of the coding benchmarks included in this tool are Python-specific.",
                    "While the HumanEval benchmark is Python-specific, extensions like HumanEval-X or MultiPLE have been developed to support additional programming languages, such as JavaScript, Java, C, C#, C++, PHP, Ruby, and Go.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Coding (HumanEval)",
                        "benchmark_measures": "Evaluates the Python generation capabilities of LLMs. It comprises 164 handcrafted programming challenges, each featuring a function signature, a descriptive docstring, and accompanying unit tests. These tasks are comparable to simple software interview questions and evaluate a model's proficiency in understanding programming concepts, algorithms, and basic mathematics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TTFT)",
                        "benchmark_measures": "Time to First Token (TTFT) measures the amount of time it takes for a language model to generate and return the very first token of its response after receiving a user prompt, essentially measuring how quickly a user starts seeing output from the model after initiating a query.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The Artificial Analysis and Vellum leaderboards both use the HumanEval benchmark where KLU uses the BigCodeBench benchmark.",
                    "All of the coding benchmarks included in this tool are Python-specific.",
                    "While the HumanEval benchmark is Python-specific, extensions like HumanEval-X or MultiPLE have been developed to support additional programming languages, such as JavaScript, Java, C, C#, C++, PHP, Ruby, and Go.",
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Python Coding",
                        "benchmark_measures": "Evaluates the Python generation capabilities of LLMs. It comprises 164 handcrafted programming challenges, each featuring a function signature, a descriptive docstring, and accompanying unit tests. These tasks are comparable to simple software interview questions and evaluate a model's proficiency in understanding programming concepts, algorithms, and basic mathematics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Generate images": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-image"
                },
                "tooltip": "The Artificial Analysis Text to Image leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The Quality vs Price bubble chart is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "Midjourney does not have an API. They approximate it using ImagineAPI, which serves as a tool to access the Midjourney Discord.",
                    "If you click on a datapiont in the charts or the Details button in the summary table at the bottom of the dashboard, you'll filter the dashboard to that model.",
                    "If a model is missing from a scatter/bubble chart, use the filter in the upper-right corner to add to it or switch out models. It'll say something like 'x out of y models'. You can also just start typing the model name when the filter is open to shave valuable seconds off your analysis time. (I'm all about efficiency. \ud83d\ude0e)",
                    "Their tooltips include the x and y values but not the z value (size), but it's not hard to tell DALLE3 HD and Ideogram v2 (at the time of writing) are infinitely slower (and more expensive) than FLUX.1[schnell].",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Generation Time, Variance' chart, a box that's positioned lower along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "I like that they use median generation time in the table at the bottom of the dashboard over mean (average). This is because it's a better metric any time you have outliers, and outliers are common with image-generation data. (I see you, DALLE3, Midjourney, and Ideogram. \ud83e\uddd0). With median, you return the middle value. This is why home prices are typically expressed as median. It's so a celeb's mansion doesn't distort the aggregated home values of a neighborhood/metro area.",
                    "Elo score is an evaluation method that involves presenting users with pairs of images generated by different models in response to the same prompt. Participants select the image they believe best matches the prompt, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, these platforms provide a transparent and continuously updated measure of model performance, reflecting the evolving landscape of AI-generated image quality.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quality Elo",
                        "benchmark_measures": "Relative ELO score of the models as determined by >100,000 responses from users in Artificial Analysis' Image Arena. Some models may not be shown due to not yet having enough votes.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "imgsys",
                "leaderboard_abbrev": "imgsys",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://imgsys.org/rankings"
                },
                "tooltip": "Developed by fal.ai, this platform presents a generative image model arena where users can compare models by selecting preferred images based on prompt adherence, semantics, and aesthetics.",
                "analysis_tips": [
                    "As an open-source initiative itself, imgsys.org focuses on evaluating and ranking models that are publicly accessible, so you won't be able to compare proprietary models here.",
                    "This leaderboard looks like a simple rank table, but it's actually a treasure trove of information. The 'Stats' button in each row allows you to compare that model against any other model in the leaderboard. It shows you the percentage of times your selected model won, lost, and tied. It's pretty clever.",
                    "There's also a Playground button in each row. Clicking it will take you to the playground page for that model, where you can actually take it for a test drive.",
                    "Next to the Playground tab is an API tab, which lets you test the API without having to root around for the documentation.",
                    "Next to each model name is an information icon. Clicking it will open a modal with summary information, e.g., model id, link to the playground, number of parameters, image size, and safety tolerance.",
                    "There are other image leaderboards, but some like Labelbox's leaderboard just have so few models, it's not worth the time to break it all down. But you can check it out at https://labelbox.com/leaderboards/image-generation/. (There were only five models at the time of writing.)"
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Elo Score",
                        "benchmark_measures": "Relative ELO score of the models. imgsys has made its calculate_elo module public, if you're so inclined to check it out: https://github.com/fal-ai/imgsys-public/blob/main/src/calculate_elo.py.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Generation Time",
                        "benchmark_measures": "Seconds to generate 1 image",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TTFT)",
                        "benchmark_measures": "Time to First Token (TTFT) measures the amount of time it takes for a language model to generate and return the very first token of its response after receiving a user prompt, essentially measuring how quickly a user starts seeing output from the model after initiating a query.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Generate text": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Communication",
                        "benchmark_measures": "Evaluates effectiveness in conveying ideas and maintaining audience engagement.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Quality Index",
                        "benchmark_measures": "Evaluates overall writing quality, including creativity, coherence, and engagement.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Reasoning & Knowledge (MMLU)",
                        "benchmark_measures": "Evaluates the model's ability to produce accurate and logical responses to prompts.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_abbrev": "Chatbot Arena",
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
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    },
                    {
                        "benchmark_name": "Longer Query",
                        "benchmark_measures": "Evaluates ability to maintain creative coherence and style in longer compositions.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    }
                ]
            },
            {
                "leaderboard": "FACTS Grounding Leaderboard",
                "leaderboard_abbrev": "FACTS",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.kaggle.com/facts-leaderboard/leaderboard"
                },
                "tooltip": "FACTS is a novel benchmark from Google DeepMind and Google Research designed to evaluate the factual accuracy and grounding of AI models.",
                "analysis_tips": [
                    "Each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request.",
                    "A response is labeled accurate if all its claims are directly supported or don't require support from the context; otherwise, it's marked inaccurate.",
                    'The eval tool uses automated LLM judge models for evaluation. In an effort to make scoring as fair as possible, they use a "range of frontier LLMs" and average the score outputs.',
                    "Where you might thinking clicking on the Factuality Score column heading would sort the column, it actually is a jump link to 'Step 4: Ensembling' lower on the page...which is unusual. That section discusses how Factuality is calculated, so I can kind of understand what they were thinking, but it's still a bit jarring from a usability standpoint.",
                    "I personally love any time a leaderboard includes a knowledge cutoff date. But since most of these models have gone agentic, it's not as essential as it used to be as they frequently search the web for answers and synthesize that information into their responses.",
                    "The full FACTS Grounding benchmark is comprised of 1,719 examples. This includes 860 public examples available in the FACTS Grounding Public Examples Dataset. The remaining 859 examples comprise a private set that will be held out to mitigate risks of benchmark contamination (i.e., model creators cheating by training their models on the test questions to boost their scores).",
                    "There are charts below the leaderboard that show the distribution of tasks (e.g., fact finding, summarizing, concept comparison, etc.) and domains (e.g., medical, legal, etc.).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Factuality",
                        "benchmark_measures": "Evaluates ability to generate factually accurate responses in information-seeking scenarios.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_abbrev": "Hugging Face",
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
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "QUAKE",
                        "benchmark_measures": "Evaluates ability to summarize and draft content in a coherent and engaging manner.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., its throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TTFT)",
                        "benchmark_measures": "Time to First Token (TTFT) measures the amount of time it takes for a language model to generate and return the very first token of its response after receiving a user prompt, essentially measuring how quickly a user starts seeing output from the model after initiating a query.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Generate video": {
        "Quality": [
            {
                # TO DO: CHECK IF IT'S STILL DOWN (404'd 12/18)
                "leaderboard": "ApolloBench",
                "leaderboard_abbrev": "ApolloBench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/Apollo-LMMs/ApolloBench"
                },
                "tooltip": "ApolloBench is a leaderboard put out by Meta and evaluates video-language models on tasks like reasoning, perception, and text recognition to measure their ability to understand and analyze video content accurately.",
                "analysis_tips": [
                    "By default, the leaderboard only shows the Overall score. You can click to reveal the other benchmark scores, which I recommend doing.",
                    "The Notes column indicates max frames but only for a few models at the time of writing.",
                    "This is the only leaderboard at the time of writing that measures a model's ability to run OCR (Optical Character Recognition) on videos.",
                    "At the time of writing the model names are clickable links, but they all 404.",
                    "You can sort the table by any column.",
                    "If model size isn't included it's because the provider doesn't disclose it."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/html/2412.10360"
                },
                "benchmarks": [
                    {
                    "benchmark_name": "Overall Accuracy",
                    "benchmark_measures": "Calculates the model's overall performance across all ApolloBench tasks, including reasoning, perception, and spatial understanding.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Egocentric",
                    "benchmark_measures": "Evaluates the model's ability to process and understand first-person perspective videos.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Spatial",
                    "benchmark_measures": "Evaluates how well the model understands spatial relationships and positioning within the video content.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "OCR (Optical Character Recognition)",
                    "benchmark_measures": "Evaluates the model's accuracy in detecting and interpreting text from videos.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Perception",
                    "benchmark_measures": "Evaluates the model's ability to recognize and understand objects, scenes, and other visual information within the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Reasoning",
                    "benchmark_measures": "Evaluates the model's logical reasoning capabilities based on visual and contextual cues in videos.",
                    "score_interpretation": "Higher is better."
                    }
                ],
            },
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-video/arena?tab=Leaderboard"
                },
                "tooltip": "This leaderboard shows the results of all votes on Video Generation Model Arena. Results are released in batches of 30 and are updated every hour.",
                "analysis_tips": [
                    "It's not apparent what the colors on the edges of the rows indicate because there's no legend at the time of writing (sigh), but ChatGPT says that black is for OpenAI (Sora), Red represents models from Kuaishou, pink represents models from MiniMax, blue represents models from Tencent, and green represents all other models.",
                    "At the time of writing the model names are clickable links, but they all 404.",
                    "All videos are converted to 720p for consistency.",
                    " "
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/text-to-video/arena?tab=Arena"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Arena Elo",
                        "benchmark_measures": "Ranking metric that quantifies a model's performance based on user preferences in head-to-head comparisons. It adjusts dynamically, awarding higher gains for defeating stronger models and stabilizing with more comparisons.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Number of Appearances",
                        "benchmark_measures": "Calculates the number of times a model's generated videos have been evaluated in head-to-head comparisons.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Eval Crafter",
                "leaderboard_abbrev": "Eval Crafter",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://evalcrafter.github.io/"
                },
                "tooltip": "This leaderboard shows the results of all votes on Video Generation Model Arena. Results are released in batches of 30 and are updated every hour.",
                "analysis_tips": [
                    "It's not apparent what the colors on the edges of the rows indicate because there's no legend at the time of writing (sigh), but ChatGPT says that black is for OpenAI (Sora), Red represents models from Kuaishou, pink represents models from MiniMax, blue represents models from Tencent, and green represents all other models.",
                    "At the time of writing the model names are clickable links, but they all 404.",
                    "All videos are converted to 720p for consistency.",
                    " "
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Visual Quality",
                        "benchmark_measures": "Evaluates the overall visual appeal of the generated video, including clarity, color accuracy, and aesthetic value.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Text-Video Alignment",
                        "benchmark_measures": "Evaluates how accurately the video content reflects the given text prompt, ensuring semantic consistency between the description and the visual output.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Motion Quality",
                        "benchmark_measures": "Evaluates the smoothness and realism of movements within the video, focusing on natural motion portrayal.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Temporal Consistency",
                        "benchmark_measures": "Evaluates the coherence of visual elements over time, ensuring that objects and scenes remain consistent throughout the video.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Final Sum Score",
                        "benchmark_measures": "A weighted aggregate of all benchmark metrics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "LongVideoBench",
                "leaderboard_abbrev": "LongVideoBench",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://longvideobench.github.io/index.html#leaderboard"
                },
                "tooltip": "This leaderboard segments video performance by video length, breaking them into four categories.",
                "analysis_tips": [
                    "The leaderboard has a column that identifies if the model is open-source or proprietary.",
                    "This leaderboard segments performance by video length, which is helpful for understanding how models perform on different types of content.",
                    "The Test Total represents the model's cumulative performance across all test subsets (e.g., 8s-15s, 15s-60s, 180s-600s, and 900s-3600s) whereas the Val Total represents the model's performance on a separate validation set.",
                    "Think of the Val Total score as a practice test score before taking the SAT. Developers can run these practice tests before submitting their model to be evaluated. The Test Total score is the actual SAT score. The validation videos are similar to the test videos but slightly different, so they don’t give away answers for the final test.",
                    "The max_frames value next to the model name indicates the maximum number of video frames the model can process or generate at one time. Models with higher max_frames can handle longer or more complex videos in one pass. This value is important for tasks like video comprehension or generation, as it reflects how much content a model can analyze or produce at once.",
                    "At the time of writing the table isn't dynamic, so you can't sort by columns or filter. If you want to have that functionality, just select the entire table and paste it into Excel or a Google Sheet (by typing 'sheet.new' in a browser).",
                    'An example question: "At the beginning of the video (0:19 - 0:22), a woman with a headband tied to her head, wearing a red top, carrying a black backpack, when the woman comes down from a hill with tall rocks (3:34 - 3:40), what changes occur to her backpack?" The model must choose from 4 options.',
                    "Click a model's name to learn more about it. It will either take you to the model's homepage, Hugging Face page, or GitHub repository.",
                    "You can view example questions on the LongVideoBench Hugging Face page: https://huggingface.co/datasets/longvideobench/LongVideoBench.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2407.15754"
                },
                "benchmarks": [
                    {
                    "benchmark_name": "Test Total",
                    "benchmark_measures": "Calculates the model's overall performance across all evaluated test clips of varying lengths, combining scores from all test subsets.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Test 8s-15s",
                    "benchmark_measures": "Evaluates the model's performance specifically on short video clips lasting between 8 to 15 seconds.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Test 15s-60s",
                    "benchmark_measures": "Evaluates how well the model performs on medium-length videos ranging from 15 to 60 seconds.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Test 180s-600s",
                    "benchmark_measures": "Evaluates the model's ability to process and understand longer videos between 3 to 10 minutes.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Test 900s-3600s",
                    "benchmark_measures": "Evaluates the model's performance on very long videos, lasting between 15 to 60 minutes, reflecting its capacity for extended content understanding.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Val Total",
                    "benchmark_measures": "Evaluates the model's performance on a separate validation set, used to ensure consistency and generalization across video lengths.",
                    "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Multi-task Long Video Understanding Benchmark",
                "leaderboard_abbrev": "Multi-task Long Video",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://github.com/JUNJIE99/MLVU"
                },
                "tooltip": "This leaderboard features a very granular approach to evaluating video generation and understanding tasks.",
                "analysis_tips": [
                    "The Mini-Leaderboard summarizes the performance of the models by including the maximum number of video frames a model can process at once ('Input'), the model size ('Size'), the mean average of its scores ('M-Avg'), and the geometic average of its scores ('G-Avg').",
                    "The geometric average is a robust measure of performance because it accounts for the variance in scores across different benchmarks. It's calculated by multiplying all the scores together, then taking a root.",
                    "Long Video Understanding requires longer context windows.",
                    "At the time of writing the table isn't dynamic, so you can't sort by columns or filter. If you want to have that functionality, just select the entire table and paste it into Excel or a Google Sheet (by typing 'sheet.new' in a browser).",
                    "Click a model's name to learn more about it. It will either take you to the model's homepage, Hugging Face page, or GitHub repository.",
                    "In the Introduction they provide three charts. Chart 1 shows the distribution of video lengths in the dataset, with most videos falling between 5-8 minutes and 8-11 minutes, while very long videos (120+ minutes) are the least common. This ensures models are evaluated on a mix of short, medium, and long durations.",
                    "Chart 2 shows a breakdown of video content types, with Surveillance (26%) and Movies (22%) being the largest categories, followed by smaller groups like Egocentric (13%) and TV Series (12%).",
                    "Chart 3 displays the distribution of tasks used to evaluate the models, split into multi-choice and generation-based tasks, with a focus on Plot QA (539 tasks), Needle QA (355 tasks), and tasks like Action Counting and Video Summarization.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/abs/2406.04264"
                },
                "benchmarks": [
                    {
                    "benchmark_name": "TR (Text Retrieval)",
                    "benchmark_measures": "Evaluates the model's ability to retrieve correct text content or captions associated with the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "AR (Action Recognition)",
                    "benchmark_measures": "Evaluates how accurately the model identifies and classifies actions occurring in the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "NQA (Natural Question Answering)",
                    "benchmark_measures": "Evaluates the model's ability to answer natural language questions based on the video's content.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "ER (Event Recognition)",
                    "benchmark_measures": "Evaluates the model's performance in identifying events or activities within the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "PQA (Programmatic Question Answering)",
                    "benchmark_measures": "Evaluates the model's ability to answer structured or programmatically generated questions about the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "SQA (Spatial Question Answering)",
                    "benchmark_measures": "Evaluates the model's ability to answer questions requiring spatial understanding of video content.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "AO (Attribute Object Recognition)",
                    "benchmark_measures": "Evaluates how well the model recognizes specific objects and their attributes within the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "AC (Action Counting)",
                    "benchmark_measures": "Evaluates the model's accuracy in counting specific actions performed within the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "TQA (Temporal Question Answering)",
                    "benchmark_measures": "Evaluates the model's ability to answer questions that require understanding of time-based events in the video.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "M-AVG (Mean Average)",
                    "benchmark_measures": "Calculates the average score across all major metrics, providing a general measure of performance.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "SSC (Scene Switch Consistency)",
                    "benchmark_measures": "Evaluates the model's ability to maintain consistent understanding across scene transitions.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "VS (Video Segmentation)",
                    "benchmark_measures": "Evaluates the model's ability to correctly segment video content into meaningful parts.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "G-Avg (Geometric Average)",
                    "benchmark_measures": "Calculates the geometric mean of selected benchmark scores to provide a robust overall performance score.",
                    "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Video-MME",
                "leaderboard_abbrev": "Video-MME",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://video-mme.github.io/home_page.html#leaderboard"
                },
                "tooltip": "This leaderboard evaluates video understanding models across tasks like action recognition, question answering, and temporal reasoning, providing comprehensive scores for performance on diverse video comprehension benchmarks.",
                "analysis_tips": [
                    "The leaderboard underscores the importance of including subtitles for higher performance in video-comprehension tasks.",
                    "The leaderboard breaks scores down by video length, which is helpful for understanding how models perform on different types of content.",
                    "Short videos are < 2 min, medium videos are 4-15 min, and long videos are 30-60 min.",
                    "By default, the leaderboard is sorted by results with subtitles. To sort by another column, click its column header. Because the sort columns are regrettably the same color as the background, it's not immediately clear that they're clickable.",
                    "Click a model's name to learn more about it. It will either take you to the model's homepage, Hugging Face page, or GitHub repository.",
                    "When the LLM Params (Large Language Model Parameters) field is empty, it typically means that the model's developers have chosen not to disclose the number of parameters.",
                    "The Date column represents the date when the model's performance was evaluated and added to the leaderboard. Green font indicates the most recent evaluations.",
                    'An example question: "On what date did the individual in the video leave a place that Simon thought was very important to him?" The model must choose from 4 options.',
                    "Video-MME consists of 6 key domains and 30 subcategories of video types. Search the leaderboard for 'benchmark statistics' to view the categories and subcategories.",
                    "There's also a distribution of video length. At the time of writing the segment with the most videos was 90 sec to 2 min.",
                    "There's also a chart with a distribution by task type.",
                    "Interestingly, they took four models and created a radar chart of their scores across question types. Search the leaderboard for 'different question types' to view it.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2405.21075"
                },
                "benchmarks": [
                    {
                    "benchmark_name": "Overall Accuracy (%)",
                    "benchmark_measures": "Calculates the model's overall performance on videos of all lengths, both with and without subtitles.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Short Video Accuracy (%)",
                    "benchmark_measures": "Evaluates how accurately the model performs on short videos, under 2 minutes, both with and without subtitles.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Medium Video Accuracy (%)",
                    "benchmark_measures": "Evaluates the model's performance on videos ranging from 4 to 15 minutes, with and without subtitles.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Long Video Accuracy (%)",
                    "benchmark_measures": "Evaluates how well the model understands long videos, between 30 to 60 minutes, with and without subtitles.",
                    "score_interpretation": "Higher is better."
                    }
                ]
            },
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed",
                        "benchmark_measures": "Output tokens per second",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Throughput",
                        "benchmark_measures": "The number of tokens the model can generate per second ('t/s')",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ]
    },
    "Solve math problems": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quantitative Reasoning (MATH)",
                        "benchmark_measures": "Evaluates mathematical reasoning and problem-solving skills across various domains.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Multilingual Maths (MGSM)",
                        "benchmark_measures": "Evaluates mathematical problem-solving across different languages and cultural contexts.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Chatbot Arena",
                "leaderboard_abbrev": "Chatbot Arena",
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
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Hugging Face Open LLM",
                "leaderboard_abbrev": "Hugging Face",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
                },
                "tooltip": "The Hugging Face Open LLM leaderboard includes several benchmarks that include math problems, but the only dedicated math benchmark is the MATH benchmark. I include it though because some of its advanced filtering options that other math leaderboards don't provide.",
                "analysis_tips": [
                    "The only benchmark that measures math exclusively is the MATH benchmark. It evaluates the model's ability to solve high school-level math problems. However, BBH, GPQA, and MMLU-PRO also include math problems in their evaluations.",
                    "This leaderboard only includes open models, so you won't find proprietary models here.",
                    "The leaderboard has a number of quick filters. At the time of writing, these include For Edge Devices, For Consumers, Mid-range, For the GPU-rich, and Only Official Providers.",
                    "The Type column uses emojis, but there's no legend. You can view what each emoji represents by hovering over it. For example, the orange diamond represents 'fine-tuned on domain-specific datasets', the speech bubble represents chat models, the pink flower represents multimodal, and the green circle represents pretrained models.",
                    "",
                    "You can remove benchmarks from the table by clicking the 'column visibility' link above the table.",
                    "The leaderboard also has a number of customization options you can choose from by clicking the 'table options' link above the table. One especially cool option is to show the rank of each model for only the columns you choose to display. You can do this by toggling Ranking Mode to Dynamic. I'd recommend filtering the table for just the MATH benchmark, and then compare the results to the table filtered for all benchmarks that include math problems (i.e., BBH, GPQA, and MMLU-PRO).",
                    "Clicking a model's name will take you to its Hugging Face page.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about"
                },
                "benchmarks": [
                   {
                    "benchmark_name": "Average",
                    "benchmark_measures": "Evaluates the overall performance of a model by calculating the weighted average of normalized scores from all benchmarks",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "IFEval",
                    "benchmark_measures": "Evaluates the model's performance on instruction-following tasks, testing its ability to respond accurately to structured prompts.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "BBH (BigBench-Hard)",
                    "benchmark_measures": "Evaluates the model's ability to handle challenging tasks requiring advanced reasoning and knowledge.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MATH",
                    "benchmark_measures": "Evaluates the model's ability to solve challenging high school-level math problems that require step-by-step reasoning.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "GPQA",
                    "benchmark_measures": "The Graduate-Level Google-Proof Q&A (GPQA) tests the model's ability to answer PhD-level multiple choice questions.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MUSR (Multistep Soft Reasoning)",
                    "benchmark_measures": "Evaluates the model's performance on multi-step reasoning tasks with longer problems, requiring logical and methodical problem-solving.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MMLU-PRO",
                    "benchmark_measures": "The Massive Multitask Language Understanding - Professional (MMLU-PRO) tests the model's knowledge and reasoning abilities across expertly reviewed multichoice questions across domains",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "CO₂ Cost",
                    "benchmark_measures": "Measures the estimated carbon emissions (in kilograms) generated during the model's evaluation process.",
                    "score_interpretation": "Lower is better."
                    }, 
                ]
            },
            {
                "leaderboard": "MathEval",
                "leaderboard_abbrev": "MathEval",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://matheval.ai/en/leaderboard/"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "A feature that sets this leaderboard apart is its segmentation feature. You can segment by language (English and Chinese at time of writing), ability (math world problems & arithmetic), grade (elementary, middle, and high school+), and shots (i.e., 'zero', 'few').",
                    "The leaderboard uses data from 20 mathematical evaluation datasets. You can view a summary of each dataset as well as example questions from each dataset on its Datasets page: https://matheval.ai/en/dataset/. Click the dataset's card to view example questions.",
                    "The leaderboard includes three aggregated metrics: Ability Average, Overall Average, and Weighted Average. The Ability Average measures the model’s accuracy on application problems and arithmetics, averaging the two for a final score. The Overall Average calculates a simple average of the model's scores across all datasets. The Weighted Average accounts for the total number of correct answers relative to the total number of questions, giving more weight to larger datasets.",
                    "So let's say Microsoft submits its math model, Phi-4, for evaluation. The Ability Average will first combine its scores across all word problems it answers, then rinse and repeat for arithmetic problems, then calculate the average of those two average scores. The Overall Average adds up its scores from all the tests—without segmenting into word and arithmetic problems—and calculates the average. The 20 datasets used to evaluate math models vary wildly in the number of questions asked, so the Weighted Average first adds up all the correct answers, then divides by the total number of questions. So a test with more questions will have a greater impact on a model's Weighted Average score.",
                    "The 'Model version date' is the official release date for each model version.",
                    "You can sort the table by any column except the 'Model version date' column.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://matheval.ai/en/leaderboard/evaluation-experiment-settings/"
                },
                "benchmarks": [
                    {
                    "benchmark_name": "Ability Average",
                    "benchmark_measures": "Calculates the model's average accuracy on application problems and arithmetic types, then averages the two as the final proficiency score.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Overall Average",
                    "benchmark_measures": "Calculates the simple average accuracy of the model across all datasets.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Weighted Average",
                    "benchmark_measures": "Divides the total number of correct answers by the total number of questions across all datasets.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "TAL-SCQ5K-EN",
                    "benchmark_measures": "Evaluates the model's ability to solve math questions in English from the TAL-SCQ5K dataset.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "TAL-SCQ5K-CN",
                    "benchmark_measures": "Evaluates the model's ability to solve math questions in Chinese from the TAL-SCQ5K dataset.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MAWPS",
                    "benchmark_measures": "Evaluates the model's performance on math word problems requiring arithmetic and reasoning skills.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "GAOKAO(Math)",
                    "benchmark_measures": "Evaluates the model's ability to solve math questions similar to China's Gaokao exam.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "GAOKAO(2023)",
                    "benchmark_measures": "Measures performance on math problems from the 2023 Gaokao math exam.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "ASDiv-A",
                    "benchmark_measures": "Evaluates accuracy on arithmetic word problems from the ASDiv-A dataset.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "CMMLU(Math)",
                    "benchmark_measures": "Tests the model’s math skills on questions from the Chinese Massive Multitask Language Understanding (CMMLU) benchmark.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MATH",
                    "benchmark_measures": "Assesses the model's ability to solve challenging high school-level math problems.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "GSM8K",
                    "benchmark_measures": "Measures performance on grade-school-level math word problems requiring step-by-step reasoning.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "MMLU(Math)",
                    "benchmark_measures": "Evaluates performance on math-related questions from the MMLU benchmark.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "SVAMP",
                    "benchmark_measures": "Tests the model’s ability to solve simple arithmetic math problems with subtle variations.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "mathQA",
                    "benchmark_measures": "Evaluates accuracy on multiple-choice math reasoning problems from the MathQA dataset.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "math23K",
                    "benchmark_measures": "Measures performance on Chinese elementary math problems requiring reasoning.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Dolphin1878",
                    "benchmark_measures": "Tests problem-solving accuracy on the Dolphin dataset of math word problems.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Ape210K",
                    "benchmark_measures": "Evaluates performance on arithmetic problems from the Ape210K dataset.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Big-Bench-Hard(Math)",
                    "benchmark_measures": "Assesses math-related questions from the BigBench-Hard benchmark, requiring advanced reasoning.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "AGIEval",
                    "benchmark_measures": "Measures performance on math problems from AGIEval, designed to test models in academic settings.",
                    "score_interpretation": "Higher is better."
                    },
                    {
                    "benchmark_name": "Arith3K",
                    "benchmark_measures": "Evaluates accuracy on arithmetic questions requiring precise numerical reasoning.",
                    "score_interpretation": "Higher is better."
                    }
                ],
            },
            {
                "leaderboard": "MathVista",
                "leaderboard_abbrev": "MathVista",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://mathvista.github.io/"
                },
                "tooltip": "MathVista is a benchmark designed to combine challenges from diverse mathematical and visual tasks. It consists of 6,141 examples, derived from 28 existing multimodal datasets involving mathematics and three newly created datasets (i.e., IQTest, FunctionQA, and PaperQA).",
                "analysis_tips": [
                    "The dashboard is broken into two leaderboards, 'testmini' and 'test' leaderboard. The testmini leaderboard includes 1,000 examples, while the test leaderboard includes all 5,141 examples.",
                    "The Human Performance row at the top indicates the average human performance by Amazon Mechanical Turk workers who were recruited to evaluate and solve the benchmark problems. They were required to at least a high school diploma to participate.",
                    "MathVista combines visual and math challenges, including puzzles, graphs, and diagrams from academic papers that test logical, algebraic, and scientific reasoning.",
                    "It also includes 9 math question datasets and 19 visual question datasets, offering 6,141 problems that combine visuals and math reasoning for a more diverse and complex evaluation.",
                    "The leaderboard includes a 'Method types' column that indicates the type of method used. These include Mixture of Experts (MoE), Large Multimodal Models (LMM), and Tool-augmented LLM (Tool). With MoE the model uses multiple specialized sub-models, LMMs process both text and images, and Tool models use external tools to solve problems, like calculators or agents.",
                    "The benchmarks are divided into two categories: Task and Math Reasoning types. The tasks include figure QA (FQA), geometry problem solving (GPS), math word problem (MWP), textbook QA (TQA), and visual QA (VQA). The Math Reasoning types include algebraic (ALG), arithmetic (ARI), geometry (GEO), logical (LOG), numeric (NUM), scientific (SCI), and statistal (STA).",
                    "The dashboard has a cool feature called the MathVista Visualizer. There are a number of filters in the left rail and example problems in the canvas.",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://arxiv.org/pdf/2310.02255"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "ALL",
                        "benchmark_measures": "Calculates the model's overall performance by averaging scores across all individual categories.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "FQA",
                        "benchmark_measures": "Evaluates the model's accuracy on factual question answering tasks.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "GPS",
                        "benchmark_measures": "Evaluates the model's ability to solve geometry problems involving spatial reasoning.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "MWP",
                        "benchmark_measures": "Evaluates the model's accuracy on math word problems.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "TQA",
                        "benchmark_measures": "Evaluates the model's performance on tasks involving textual quantitative analysis.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "VQA",
                        "benchmark_measures": "Evaluates the model's ability to solve visual question answering tasks.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "ALG",
                        "benchmark_measures": "Evaluates the model's ability to solve algebra-related problems.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "ARI",
                        "benchmark_measures": "Evaluates the model's accuracy on arithmetic-based reasoning problems.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "GEO",
                        "benchmark_measures": "Evaluates the model's performance on general geometry problems.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "LOG",
                        "benchmark_measures": "Evaluates the model's logical reasoning abilities on tasks requiring deductive logic.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "NUM",
                        "benchmark_measures": "Evaluates the model's numerical computation and problem-solving abilities.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "SCI",
                        "benchmark_measures": "Evaluates the model's performance on science-related reasoning and problem-solving tasks.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "STA",
                        "benchmark_measures": "Evaluates the model's ability to solve problems involving statistical analysis.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The math-leaning benchmarks from least to most difficult: 'GSM8K' (KLU/Vellum): grade school word problems; 'MATH' (KLU/Vellum): high school math (algebra, geometry, intro calculus); MATH-500 (Artificial Analysis): university-level math problems. I didn't include Chat Arena's MT-Bench benchmark (which it labels 'Math') because its focus is on assessing multi-turn conversation, which has some math overlap. It would be good to look at to see maybe a hybrid of chat and math (think Khan Academy's chatbot, Khanmigo), but since it's not a pure math benchmark, I left it out.",
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Hard Math (MATH-500)",
                        "benchmark_measures": "University-level math problems (algebra, calculus, geometry, and number theory)",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Easy Math (GSM8K)",
                        "benchmark_measures": "Grade school word problems",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).", # LEFT OFF
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TPS)",
                        "benchmark_measures": "Tokens Per Second (TPS) measures the number of tokens a model can process per second, i.e., throughput.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The math-leaning benchmarks from least to most difficult: 'GSM8K' (KLU/Vellum): grade school word problems; 'MATH' (KLU/Vellum): high school math (algebra, geometry, intro calculus); MATH-500 (Artificial Analysis): university-level math problems. I didn't include Chat Arena's MT-Bench benchmark (which it labels 'Math') because its focus is on assessing multi-turn conversation, which has some math overlap. It would be good to look at to see maybe a hybrid of chat and math (think Khan Academy's chatbot, Khanmigo), but since it's not a pure math benchmark, I left it out.",
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Math Problems (MATH)",
                        "benchmark_measures": "High school math (algebra, geometry, intro calculus)",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Grade School Math (GSM8K)",
                        "benchmark_measures": "Grade school word problems",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent. For models which do not support streaming, this represents time to receive the completion.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "KLU didn't have a methodology page at the time of writing, but they have an FAQ section below the leaderboard, which touches on their methodology.",
                    "One thing that could be confusing is at the time of writing KLU has two different columns in their tables labeled 'SPEED'. One measures tokens per second (TPS) where the other measures time to first token (TTFT). I categorize TTFT as latency, not speed.",
                    "The goal is to have lower latency (TTFT) and higher throughput TPS.", 
                    "One thing I like about this leaderboard is the ability to compare two models side by side. (Search for 'Frontier Model Comparison'. This is a nice feature when you've narrowed your model choices down to a couple.)", 
                    "At the time of writing, the leaderboard listed Claud 3 Opus as having the largest context window, with 200k. However, they track Gemini 1.5 Pro, which has a 2m token context window, so this leaderboard (or at least the summary metrics at the top of the leaderboard).",
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed (TTFT)",
                        "benchmark_measures": "Time to First Token (TTFT) measures the amount of time it takes for a language model to generate and return the very first token of its response after receiving a user prompt, essentially measuring how quickly a user starts seeing output from the model after initiating a query.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Latency",
                        "benchmark_measures": "Time to first token of tokens received, in seconds, after API request sent.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "These speed scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower speed but higher quality and at a fraction of the cost , it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "I love their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Their breakdown of context windows is very helpful. At the time of writing Google is crushing the competition.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price",
                        "benchmark_measures": "Price per token, represented as USD per million Tokens. Price is a blend of Input & Output token prices (3:1 ratio).",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_abbrev": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Cost can vary from one API provider to another.It's risky to compare cost from one leaderboard to another because they may calculate cost differently. For example, Artificial Analysis calculates cost based on a blend of input and output tokens, while it's not clear how KLU calculates cost. They don't disclose how this benchmark is calculated on their leaderboard at time of writing.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Cost / 1m tokens",
                        "benchmark_measures": "The leaderboard does not specify whether these costs are calculated based on input tokens, output tokens, or a combination of both.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Input cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    },
                    {
                        "benchmark_name": "Output cost",
                        "benchmark_measures": "Measured per million tokens",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Context window": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "In the 'Further details' section they provide a link to the API Providers for each model, which is incredibly helpful. There can be significant differences in cost and performance from one provider to another.",
                    "I \ud83d\udc9a their use of bubble charts to visualize their performance data because it provides context. And they make them even more useful by coloring the 'most attractive quadrant' green and the least attractive gray.",
                    "Each of their charts comes equipped with a model filter. You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "Search the dashboard for 'context window' to jump to the charts that include it as a metric. At the time of writing, Google is crushing the competition. They're the only models in the green quadrant of the 'Quality vs. Context window, Input Token Price' chart and they crush the other bars in the 'Content Window' bar chart.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Vellum LLM Leaderboard",
                "leaderboard_abbrev": "Vellum",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "tooltip": "The Vellum LLM leaderboard isn't updated as frequently as most, but it's simplicity defined, which could be a good place to cut your teeth on leaderboards.",
                "analysis_tips": [
                    "The primary value in Vellum's leaderboard is its ability to select two models and compare them. If you don't need the most current models or happen to use it after it's been updated, this could be a great resource.",
                    "The last updated date is at the bottom of the page. A lot can change in a few months' time, so keep that in mind, if the leaderboard hasn't been updated recently.",
                    "I really like that this leaderboard includes cutoff dates. Most do not. But given how infrequently it's updated, you need to verify these dates.",
                    "I also like that they simplify the metrics and provide the official, super-geeky name in a tooltip. So 'MMLU Benchmark' becomes 'Multiple choice Qs' and 'BBHard Benchmark' becomes 'Future Capabilities'."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://www.vellum.ai/llm-leaderboard"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ]
    },
    "Convert speech to text": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/speech-to-text"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for speech-to-text capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Word Error Rate vs. Price scatterplot is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "They shoehorn a lot of extra information in information icons in the table at the bottom of the chart.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Speed Factor, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "I like that they use median speed factor in the table at the bottom of the dashboard over mean (average). This is because it's a better metric any time you have outliers, and outliers are common with image-generation data. (I see you, DALLE3, Midjourney, and Ideogram. \ud83e\uddd0). With median, you return the middle value. This is why home prices are typically expressed as median. It's so a celeb's mansion doesn't distort the aggregated home values of a neighborhood/metro area.",
                    "Elo score is an evaluation method that involves presenting users with pairs of transcripts and prompts generated by different models in response to the same prompt. Participants select the transcription they believe best matches the prompt, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, these platforms provide a transparent and continuously updated measure of model performance, reflecting the evolving landscape of AI-generated image quality.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/speech-to-text/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Word Error Rate",
                        "benchmark_measures": "Percentage of words incorrect in the transcription.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            },
            {
                "leaderboard": "Open ASR (Hugging Face)",
                "leaderboard_abbrev": "Open ASR",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/hf-audio/open_asr_leaderboard"
                },
                "tooltip": "The Open ASR Leaderboard ranks and evaluates speech recognition models on the Hugging Face Hub.",
                "analysis_tips": [
                    "At the time of writing the leaderboard only includes English speech recognition, but they plan to expand to multilingual evaluation in later versions.",
                    "Clicking on a model opens a page with detailed information about how it was tested. You can also find out useful information about the model, such as how many languages it supports, with a click-to-reveal toggle to view the supported languages.",
                    "Other important details in the model page are its sampling rate, license type, GitHub repo link (as Hugging Face focuses on open models), MMS checkpoints, etc.",
                    "The only two benchmarks in the table are Word Error Rate (WER) and Inverse Real-Time Factor (RTFx). The additional columns (e.g., AMI, Earnings22, Gigaspeech, etc.) correspond to benchmark datasets used to evaluate model performance. They reference the WER achieved by the model on that dataset. You can also sort the table by these scores.",
                    "There's a Metrics tab where you can learn more about the benchmark metrics the leaderboard uses.",
                    "At the bottom of the Metrics tab there is a table with more information about each of the datasets used to test models, e.g., speaking style, license info, types of audio it transcribes (i.e., its domain), etc."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/speech-to-text/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Word Error Rate",
                        "benchmark_measures": "Percentage of words incorrect in the transcription.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis STT",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/speech-to-text"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for speech-to-text capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Word Error Rate vs. Price scatterplot is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "They shoehorn a lot of extra information in information icons in the table at the bottom of the chart.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Speed Factor, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "I like that they use median speed factor in the table at the bottom of the dashboard over mean (average). This is because it's a better metric any time you have outliers, and outliers are common with image-generation data. (I see you, DALLE3, Midjourney, and Ideogram. \ud83e\uddd0). With median, you return the middle value. This is why home prices are typically expressed as median. It's so a celeb's mansion doesn't distort the aggregated home values of a neighborhood/metro area.",
                    "Elo score is an evaluation method that involves presenting users with pairs of transcripts and prompts generated by different models in response to the same prompt. Participants select the transcription they believe best matches the prompt, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, these platforms provide a transparent and continuously updated measure of model performance, reflecting the evolving landscape of AI-generated image quality.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/speech-to-text/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Speed Factor",
                        "benchmark_measures": "The ratio of audio duration to the time taken for transcription; a Speed Factor above 1 indicates faster-than-real-time transcription (e.g., a factor of 2.0 means a 10-minute audio file is transcribed in 5 minutes).",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis STT",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/speech-to-text"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for speech-to-text capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Word Error Rate vs. Price scatterplot is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "They shoehorn a lot of extra information in information icons in the table at the bottom of the chart.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Speed Factor, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "I like that they use median speed factor in the table at the bottom of the dashboard over mean (average). This is because it's a better metric any time you have outliers, and outliers are common with image-generation data. (I see you, DALLE3, Midjourney, and Ideogram. \ud83e\uddd0). With median, you return the middle value. This is why home prices are typically expressed as median. It's so a celeb's mansion doesn't distort the aggregated home values of a neighborhood/metro area.",
                    "Elo score is an evaluation method that involves presenting users with pairs of transcripts and prompts generated by different models in response to the same prompt. Participants select the transcription they believe best matches the prompt, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, these platforms provide a transparent and continuously updated measure of model performance, reflecting the evolving landscape of AI-generated image quality.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/speech-to-text/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price per 1,000 Minutes",
                        "benchmark_measures": "The cost in USD to transcribe 1,000 minutes of audio, based on real-time audio duration; for providers charging by processing time, costs are estimated accordingly.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ]
    },
    "Convert text to speech": {
        "Quality": [
            {
                "leaderboard": "Artificial Analysis TTS",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-speech"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for text-to-speech capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Quality vs Price bubble chart (which uses speed to size) is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "The table at the bottom of the dashboard has a column that lets you know if the model supports streaming. Streaming support is very important if you need to generate speech in real time. A model might be very fast (e.g., 'Studio, Google Cloud TTS' coming in hot at 283.3 characters per second at the time of writing) and at quite the premium ($160 per 1m characters), but if it doesn't support streaming, it's not going to be useful for real-time applications. Meanwhile, the 'Turbo v2.5, ElevenLabs' is cheaper, faster, has a higher Elo score, and supports streaming, illustrating why these leaderboards are so important.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Characters Per Second, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "Elo score is an evaluation method that involves presenting users with pairs of audio samples generated by different text-to-speech models from the same text input. Participants select the sample they believe is more natural or aligns better with the text, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, this leaderboard provides a transparent and continuously updated measure of model performance, reflecting advancements in AI-generated speech quality.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Quality ELO",
                        "benchmark_measures": "Evaluates the naturalness and overall quality of the generated speech based on user preferences in pairwise comparisons.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "TTS Arena",
                "leaderboard_abbrev": "TTS Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/spaces/TTS-AGI/TTS-Arena"
                },
                "tooltip": "TTS Arena is a community-driven platform where users can listen to audio samples generated by different TTS models and vote on their preferences. It then displays models in descending order of how natural they sound (based on votes cast by the community).",
                "analysis_tips": [
                    "TTS Arena uses AJAX, so I can't link to a tab. If you click through to the leaderboard or methodology link, you'll then either need to select the Leaderboard or About tab.",
                    "They selected several SOTA (State of the Art) models for their leaderboard. While most are open-source models, they also included several proprietary models to allow developers to compare the state of open-source development with proprietary models.",
                    "In order to help keep results fair, the leaderboard hides results by default until the number of votes passes a threshold.",
                    "Click the 'Reveal preliminary results' toggle to show models without sufficient votes.",
                    "You can also exclude votes obtained through Battle Mode by selecting the 'Hide Battle Mode votes' toggle.",
                    "The only two benchmarks in the table are Word Error Rate (WER) and Inverse Real-Time Factor (RTFx). The additional columns (e.g., AMI, Earnings22, Gigaspeech, etc.) correspond to benchmark datasets used to evaluate model performance. They reference the WER achieved by the model on that dataset. You can also sort the table by these scores.",
                    "There's a Metrics tab where you can learn more about the benchmark metrics the leaderboard uses.",
                    "At the bottom of the Metrics tab there is a table with more information about each of the datasets used to test models, e.g., speaking style, license info, types of audio it transcribes (i.e., its domain), etc.",
                    "The impetus for this leaderboard is metrics like WER (word error rate) are often unreliable measures of model quality as a model can have a low WER but still sound unnatural. This platform aims to provide a more human-centric evaluation of TTS models."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://huggingface.co/spaces/TTS-AGI/TTS-Arena"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Score",
                        "benchmark_measures": "A model's Elo rating, determined by how frequently a model's audio outputs are preferred in direct user comparisons, factoring in the difficulty of its competition",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis TTS",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-speech"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for text-to-speech capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Quality vs Price bubble chart (which uses speed to size) is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "The table at the bottom of the dashboard has a column that lets you know if the model supports streaming. Streaming support is very important if you need to generate speech in real time. A model might be very fast (e.g., 'Studio, Google Cloud TTS' coming in hot at 283.3 characters per second at the time of writing) and at quite the premium ($160 per 1m characters), but if it doesn't support streaming, it's not going to be useful for real-time applications. Meanwhile, the 'Turbo v2.5, ElevenLabs' is cheaper, faster, has a higher Elo score, and supports streaming, illustrating why these leaderboards are so important.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Characters Per Second, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "Elo score is an evaluation method that involves presenting users with pairs of audio samples generated by different text-to-speech models from the same text input. Participants select the sample they believe is more natural or aligns better with the text, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, this leaderboard provides a transparent and continuously updated measure of model performance, reflecting advancements in AI-generated speech quality.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Characters per Second",
                        "benchmark_measures": "Evaluates the processing speed by measuring the number of text characters converted to speech per second during generation.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis TTS",
                "leaderboard_abbrev": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/text-to-speech"
                },
                "tooltip": "Artificial Analysis provides comprehensive metrics for text-to-speech capabilities, focusing on production-ready models.",
                "analysis_tips": [
                    "The Quality vs Price bubble chart (which uses speed to size) is eye opening. I highly recommend spending time analyzing it before investing in a model.",
                    "The scatter/bubble charts highlight the ideal quadrant in green and the least desirable quadrant in gray, which is brilliant.",
                    "The table at the bottom of the dashboard has a column that lets you know if the model supports streaming. Streaming support is very important if you need to generate speech in real time. A model might be very fast (e.g., 'Studio, Google Cloud TTS' coming in hot at 283.3 characters per second at the time of writing) and at quite the premium ($160 per 1m characters), but if it doesn't support streaming, it's not going to be useful for real-time applications. Meanwhile, the 'Turbo v2.5, ElevenLabs' is cheaper, faster, has a higher Elo score, and supports streaming, illustrating why these leaderboards are so important.",
                    "I \ud83d\udc9a that they include a boxplot, but they can be harder to interpret for neophytes. Essentially, the line in the middle of the box indicates the mean (average); the tails the spread (sans outliers); and the height variance. So in the 'Characters Per Second, Variance' chart, a box that's positioned higher along the y axis is faster, and a short box indicates it's consistent in its performance, whereas a tall box indicates there's a lot of variance from test to test. Think of it like the kid who consistently gets good (or bad) grades on tests versus a kid whose performance can vary wildly from test to test. They are an unsung hero of statistical analysis, but once you get used to them, it's hard to go back to pie and bar charts.",
                    "Elo score is an evaluation method that involves presenting users with pairs of audio samples generated by different text-to-speech models from the same text input. Participants select the sample they believe is more natural or aligns better with the text, and these choices are used to calculate each model's Elo score. By adopting the Elo rating system, this leaderboard provides a transparent and continuously updated measure of model performance, reflecting advancements in AI-generated speech quality.",
                    "Next to their charts is a model filter. They only show 15 of the available 19 models (at the time of writing). You can switch out those models for other models, especially as you inch your way closer to a decision on a model."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Price per 1M Characters",
                        "benchmark_measures": "Indicates the cost associated with generating speech for one million characters of text.",
                        "score_interpretation": "Lower is better."
                    }
                ]
            }
        ]
    }
}