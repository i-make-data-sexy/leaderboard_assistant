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
            "Context Window"
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
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
                        "benchmark_measures": "Assesses practical, multi-step problem-solving, which is fundamental for chain agents orchestrating tasks across different tools.",
                        "score_interpretation": "Higher scores are better."
                    }
                ]
            },
            {
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                        "benchmark_measures": "Measures the model's performance in conversational settings, evaluating communication skills, coherence, and engagement based on user feedback.",
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate superior conversational ability, as judged by one-to-one comparisons."
                    }
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
                        "score_interpretation": "Score ranges from 1 \u2013 thousands (higher is better)."
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
                        "benchmark_measures": "Tests model's ability to follow explicit formatting instructions.",
                        "score_interpretation": "Higher scores indicate better adherence to instructions."
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores reflect better ability to perform chained reasoning."
                    }
                ]
            },
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Quality",
                        "benchmark_measures": "Evaluates the model's overall ability across reasoning, instruction-following, text generation, and domain-specific tasks such as math and coding.",
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                        "benchmark_measures": "Assesses graduate-level reasoning and problem-solving.",
                        "score_interpretation": "Higher is better."
                    }
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
                        "benchmark_name": "Hard Prompts (Overall)",
                        "benchmark_measures": "Evaluates performance on complex, multi-step reasoning challenges.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    },
                    {
                        "benchmark_name": "Multi-Turn Reasoning",
                        "benchmark_measures": "Tests ability to maintain logical consistency across extended reasoning chains.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
                    },
                    {
                        "benchmark_name": "Complex Problem Solving",
                        "benchmark_measures": "Assesses ability to solve problems requiring multiple steps and consideration of various factors.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
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
                        "score_interpretation": "Higher scores indicate better complex reasoning capabilities."
                    },
                    {
                        "benchmark_name": "MUSR",
                        "benchmark_measures": "Evaluates performance on multi-step reasoning tasks.",
                        "score_interpretation": "Higher scores indicate better sequential reasoning ability."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
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
                        "benchmark_measures": "Assesses challenging, multi-step problem-solving.",
                        "score_interpretation": "Higher scores are better."
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
                        "score_interpretation": "Scores range from 0\u2013100 pct (higher is better), with a score of 65 pct or greater being classified as equivalent to a human expert."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                        "score_interpretation": "Higher Arena Scores and lower Rank indicate greater coding proficiency and correctness."
                    }
                ]
            },
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
                        "score_interpretation": "Higher scores indicate better performance, emphasizing usability and real-world applicability over strict correctness."
                    },
                    {
                        "benchmark_name": "Pass@1 (Raw)",
                        "benchmark_measures": "The percentage of tasks solved correctly by the first attempt, without calibration for omissions or partial correctness.",
                        "score_interpretation": "Higher scores indicate stricter correctness with no allowance for omissions."
                    }
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
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
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
                    "The leaderboard is divided into different tasks: clone detection, defect detection, cloze test, code completion, code refinement, code translation, type prediction, natural language code search, code generation, code summarization, and documentation translation. Because Microsoft, amirite? Check which specific task is most relevant to your needs.",
                    "Because the guidelines for submitting models are so stringent and the datasets often require significant preprocessing, not many models participate so keep that in mind when considering this leaderboard.",
                    "One advantage to CodeXGLUE is it's more representative of programming languages besides Python.",
                    "If a column is cut off, hover over a column border and drag it to the left to make room for the obstructed column."
                ],
                "benchmarks": [
                    {
                        "benchmark_name": "Overall",
                        "benchmark_measures": "Aggregates performance across all CodeXGLUE tasks to evaluate general code intelligence capabilities",
                        "score_interpretation": "Higher scores indicate better overall performance across all benchmarks"
                    },
                    {
                        "benchmark_name": "Clone Detection (Code-Code)",
                        "benchmark_measures": "Identifies semantically equivalent code snippets despite syntactic differences",
                        "score_interpretation": "Higher F1 scores indicate better clone detection accuracy"
                    },
                    {
                        "benchmark_name": "Defect Detection (Code-Code)",
                        "benchmark_measures": "Evaluates ability to identify bugs and potential defects in code",
                        "score_interpretation": "Higher accuracy indicates better defect detection"
                    },
                    {
                        "benchmark_name": "Cloze Test (Code-Code)",
                        "benchmark_measures": "Tests understanding of code context by predicting masked tokens in code sequences",
                        "score_interpretation": "Higher accuracy scores indicate better token prediction ability"
                    },
                    {
                        "benchmark_name": "Code Completion (Code-Code)",
                        "benchmark_measures": "Measures ability to autocomplete partial code snippets with contextually appropriate suggestions",
                        "score_interpretation": "Higher accuracy and BLEU scores indicate better completion quality"
                    },
                    {
                        "benchmark_name": "Code Refinement (Code-Code)",
                        "benchmark_measures": "Evaluates capacity to improve code quality through bug fixes and optimizations",
                        "score_interpretation": "Higher accuracy and lower error rates indicate better refinement capabilities"
                    },
                    {
                        "benchmark_name": "Code Translation (Code-Code)",
                        "benchmark_measures": "Tests ability to convert code between different programming languages while preserving functionality",
                        "score_interpretation": "Higher functional equivalence scores indicate better translation accuracy"
                    },
                    {
                        "benchmark_name": "Type Prediction (Code-Code)",
                        "benchmark_measures": "Predicts variable and function types in dynamically typed languages",
                        "score_interpretation": "Higher accuracy indicates better type inference capabilities"
                    },
                    {
                        "benchmark_name": "Natural Language Code Search (Text-Code)",
                        "benchmark_measures": "Evaluates effectiveness in finding relevant code snippets based on natural language queries",
                        "score_interpretation": "Higher MRR and NDCG scores indicate better search accuracy"
                    },
                    {
                        "benchmark_name": "Code Generation (Text-Code)",
                        "benchmark_measures": "Evaluates ability to create executable code from natural language descriptions",
                        "score_interpretation": "Higher BLEU and exact match scores indicate better generation accuracy"
                    },
                    {
                        "benchmark_name": "Code Summarization (Code-Text)",
                        "benchmark_measures": "Tests capacity to generate concise natural language descriptions of code functionality",
                        "score_interpretation": "Higher BLEU and ROUGE scores indicate better summarization quality"
                    },
                    {
                        "benchmark_name": "Documentation Translation (Text-Text)",
                        "benchmark_measures": "Measures accuracy in translating technical documentation between different human languages",
                        "score_interpretation": "Higher BLEU scores indicate better translation quality"
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
                        "score_interpretation": "Higher scores reflect greater proficiency in coding tasks."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_measures": "Assesses the Python generation capabilities of LLMs. It comprises 164 handcrafted programming challenges, each featuring a function signature, a descriptive docstring, and accompanying unit tests. These tasks are comparable to simple software interview questions and evaluate a model's proficiency in understanding programming concepts, algorithms, and basic mathematics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The Artificial Analysis and Vellum leaderboards both use the HumanEval benchmark where KLU uses the BigCodeBench benchmark.",
                    "All of the coding benchmarks included in this tool are Python-specific.",
                    "While the HumanEval benchmark is Python-specific, extensions like HumanEval-X or MultiPLE have been developed to support additional programming languages, such as JavaScript, Java, C, C#, C++, PHP, Ruby, and Go.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "BCB Coding (BigCodeBench)",
                        "benchmark_measures": "Assesses the Python generation capabilities of an LLM by its performance in realistic programming scenarios. It's comprised of 1,140 function-level tasks that challenge models to utilize multiple function calls from 139 libraries across seven domains, including data analysis and web development. The tasks feature complex instructions and diverse function calls, aiming to assess models' abilities to understand intricate requirements and generate appropriate code solutions.",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_measures": "It uses the HumanEval benchmark to assess the Python generation capabilities of LLMs. It comprises 164 handcrafted programming challenges, each featuring a function signature, a descriptive docstring, and accompanying unit tests. These tasks are comparable to simple software interview questions and evaluate a model's proficiency in understanding programming concepts, algorithms, and basic mathematics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Cost": [
            {
                "leaderboard": "Artificial Analysis",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Vellum LLM Leaderboard",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                        "benchmark_measures": "Assesses effectiveness in conveying ideas and maintaining audience engagement.",
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
                        "benchmark_measures": "Tests ability to maintain creative coherence and style in longer compositions.",
                        "score_interpretation": "If you are sorting by rank (the default), the score ranges from 1 to the number of models and a lower score is better. If you sort by Arena Score higher is better."
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
                        "score_interpretation": "Higher scores indicate better writing accuracy and quality."
                    }
                ]
            },
            {
                "leaderboard": "KLU",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
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
                        "benchmark_measures": "Assesses ability to summarize and draft content in a coherent and engaging manner.",
                        "score_interpretation": "Higher scores are better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                "leaderboard": "Artificial Analysis",
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
                "paper": {
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
                        "benchmark_measures": "Measures the number of times a model's generated videos have been evaluated in head-to-head comparisons.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "Eval Crafter",
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
                "paper": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Visual Quality",
                        "benchmark_measures": "Assesses the overall visual appeal of the generated video, including clarity, color accuracy, and aesthetic value.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Text-Video Alignment",
                        "benchmark_measures": "Evaluates how accurately the video content reflects the given text prompt, ensuring semantic consistency between the description and the visual output.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Motion Quality",
                        "benchmark_measures": "Analyzes the smoothness and realism of movements within the video, focusing on natural motion portrayal.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Temporal Consistency",
                        "benchmark_measures": "Examines the coherence of visual elements over time, ensuring that objects and scenes remain consistent throughout the video.",
                        "score_interpretation": "Higher is better."
                    },
                    {
                        "benchmark_name": "Final Sum Score",
                        "benchmark_measures": "A weighted aggregate of all benchmark metrics.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                        "score_interpretation": "Higher scores indicate better overall performance in reasoning, coherence, and content generation across various tasks."
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
                        "score_interpretation": "Higher is better as it signifies better performance."
                    }
                ]
            }
        ],
        "Latency": [
            {
                "leaderboard": "Artificial Analysis",
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
                        "benchmark_measures": "Tests mathematical reasoning and problem-solving skills across various domains.",
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
                        "score_interpretation": "Higher scores indicate better advanced mathematical capabilities."
                    },
                    {
                        "benchmark_name": "MATH Lvl 5 Raw",
                        "benchmark_measures": "Provides unprocessed scores from Level 5 MATH dataset evaluations.",
                        "score_interpretation": "Higher scores reflect better raw performance on advanced mathematics."
                    },
                    {
                        "benchmark_name": "GSM8K",
                        "benchmark_measures": "Evaluates ability to solve grade school math word problems.",
                        "score_interpretation": "Higher scores indicate better practical math problem-solving ability."
                    }
                ]
            },
            {
                "leaderboard": "MathEval",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://matheval.ai/en/leaderboard/"
                }
            }
        ],
        "Speed": [
            {
                "leaderboard": "Artificial Analysis",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://artificialanalysis.ai/models"
                },
                "tooltip": "The Artificial Analysis Quality Evaluations leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "The math-leaning benchmarks from least to most difficult: 'GSM8K' (KLU/Vellum): grade school word problems; 'MATH' (KLU/Vellum): high school math (algebra, geometry, intro calculus); MATH-500 (Artificial Analysis): university-level math problems. I didn't include Chat Arena's MT-Bench benchmark (which it labels 'Math') because its focus is on assessing multi-turn conversation, which has some math overlap. It would be good to look at to see maybe a hybrid of chat and math (think Khan Academy's chatbot, Khanmigo), but since it's not a pure math benchmark, I left it out.",
                    "Speed is included in the 'Quality Evaluations', 'Performance Summary', 'Speed', and 'Total Response Time' sections of their leaderboard.",
                    "They shorten their 'Quality Index' benchmark to 'Quality' in their charts.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
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
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://klu.ai/llm-leaderboard"
                },
                "tooltip": "The KLU leaderboard evaluates LLMs based on their own set of independent metrics.",
                "analysis_tips": [
                    "Higher is better.",
                    "The math-leaning benchmarks from least to most difficult: 'GSM8K' (KLU/Vellum): grade school word problems; 'MATH' (KLU/Vellum): high school math (algebra, geometry, intro calculus); MATH-500 (Artificial Analysis): university-level math problems. I didn't include Chat Arena's MT-Bench benchmark (which it labels 'Math') because its focus is on assessing multi-turn conversation, which has some math overlap. It would be good to look at to see maybe a hybrid of chat and math (think Khan Academy's chatbot, Khanmigo), but since it's not a pure math benchmark, I left it out.",
                    "These quality scores are best evaluated against other performance metrics, imo. (IOW, I'm a bigger fan of scatterplots than bar charts.) For example, if you find a model that has slightly lower quality but at a fraction of the cost with similar speed and lower latency, it might be a better choice overall. So take some time to check out their scatterplots on the same page.",
                    "It's important to understand that the Artificial Analysis and KLU leaderboards measure speed differently. Artificial Analysis breaks it down into two metrics: latency (time to generate the first token) and tokens per second (TPS) (rate of token generation). KLU, on the other hand, measures inference speed, which looks at the total time to process input and generate the entire output without breaking it into latency or TPS components. So you can't do an apples-to-apples comparison between the two leaderboards.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Hard Math (MATH)",
                        "benchmark_measures": "High school math (algebra, geometry, intro calculus)",
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
                "leaderboard": "Vellum LLM Leaderboard",
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
        "Context Window": [
            {
                "leaderboard": "Artificial Analysis",
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
                    "Search the dashboard for 'context window' to jump to the charts that include it as a metric. At the time of writing, Google is crushing the competition. They're the only models in the green quadrant of the 'Quality vs. Context Window, Input Token Price' chart and they crush the other bars in the 'Content Window' bar chart.",
                    "The 'What LLM Provider' leaderboard (which is based on Artificial Analysis' data) is a great resource for comparing metrics (https://whatllm.vercel.app/). You can choose your x and y axes (a man after my own heart) and also apply filters, e.g., Minimum Model Performance Index and Maximum Cost."
                ],
                "methodology": {
                    "text": "Methodology",
                    "url": "https://artificialanalysis.ai/methodology"
                },
                "benchmarks": [
                    {
                        "benchmark_name": "Context Window",
                        "benchmark_measures": "Maximum number of combined input & output tokens. Output tokens commonly have a significantly lower limit (varies by model).",
                        "score_interpretation": "Higher is better."
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
                        "benchmark_name": "Context Window",
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
                "leaderboard": "Artificial Analysis STT",
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
                "leaderboard": "Open ASR",
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
                        "benchmark_measures": "Assesses the naturalness and overall quality of the generated speech based on user preferences in pairwise comparisons.",
                        "score_interpretation": "Higher is better."
                    }
                ]
            },
            {
                "leaderboard": "TTS Arena",
                "leaderboard_link": {
                    "text": "View leaderboard",
                    "url": "https://huggingface.co/blog/arena-tts"
                },
                "tooltip": "TTS Arena is a community-driven platform where users can listen to audio samples generated by different TTS models and vote on their preferences. It then displays models in descending order of how natural they sound (based on votes cast by the community).",
                "analysis_tips": [
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