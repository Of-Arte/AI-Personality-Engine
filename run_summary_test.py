import json
from engine import build_full_profile

# Example profile template
example_profile = {
    "model_preference": "GPT-5",
    "formality": "Balanced",
    "tone": "Optimistic",
    "decision_style": "Data-driven",
    "risk_tolerance": "Moderate",
    "creativity_level": "High",
    "ethical_priorities": "Fairness and honesty",
    "communication_style": "Concise but empathetic",
    "patience_level": "High",
    "humor_preference": "Occasional light humor",
    "goal_focus": "Practical problem solving",
    "collaboration_preference": "Co-creative",
    "feedback_style": "Direct but constructive",
    "time_horizon": "Medium-term (weeks to months)",
    "personality_traits": ["curious", "methodical", "adaptive"]
}

# 10 varied simulated response sets
simulated_response_sets = [
    # 1 - Structured, cautious, moderate risk
    {
        "q1": "Structured",
        "q4": "I prefer structured step-by-step guidance but like occasional creative suggestions.",
        "q12": "I enjoy tasks where creativity is key, especially when brainstorming solutions.",
        "q18": "I test AI suggestions but rely on my judgment when deadlines are tight.",
        "q37": "I adapt quickly to changes but prefer some structure to stay organized.",
        "q42": "I value fairness in decisions but can prioritize pragmatic results when necessary."
    },
    # 2 - Hands-on experimentation, high risk
    {
        "q1": "Hands-on experimentation",
        "q4": "I often experiment freely, trying unconventional solutions until I find what works.",
        "q12": "Creativity is essential; I like to brainstorm outside traditional methods.",
        "q18": "I experiment under pressure and adjust rapidly based on results.",
        "q37": "I learn from mistakes quickly and adapt without overthinking.",
        "q42": "I try to innovate while keeping some structure to avoid chaos."
    },
    # 3 - Quick overview, low risk
    {
        "q1": "Quick overview",
        "q4": "I like to get a general sense first, then dive deeper if needed.",
        "q12": "Creativity is nice-to-have but not essential for my tasks.",
        "q18": "I evaluate AI suggestions cautiously before acting.",
        "q37": "I observe first, then implement gradually.",
        "q42": "I follow rules but incorporate small personal tweaks when appropriate."
    },
    # 4 - Explore examples yourself, moderate-high creativity
    {
        "q1": "Explore examples yourself",
        "q4": "I review examples and try to derive my own methods from them.",
        "q12": "I like creative problem-solving but within structured boundaries.",
        "q18": "I test AI outputs experimentally and adapt them to my context.",
        "q37": "I quickly adjust to changes by learning from examples.",
        "q42": "I combine creative and structured approaches when solving tasks."
    },
    # 5 - Step-by-step collaboration, high patience
    {
        "q1": "Step-by-step detailed guidance",
        "q4": "I follow stepwise instructions closely but add small creative touches.",
        "q12": "Creativity is important for fine-tuning solutions.",
        "q18": "I methodically test AI suggestions and adapt cautiously.",
        "q37": "I am patient and deliberate when adapting to new tasks.",
        "q42": "I integrate creativity into structured workflows."
    },
    # 6 - Open-ended co-creative, high risk, high creativity
    {
        "q1": "Hands-on experimentation",
        "q4": "I collaborate with AI to co-create and test unconventional ideas.",
        "q12": "Creativity is essential; I explore all possibilities.",
        "q18": "I take risks to achieve innovative outcomes under pressure.",
        "q37": "I adapt rapidly and embrace uncertainty.",
        "q42": "I combine innovation with minimal structure."
    },
    # 7 - Solo/guided, low patience
    {
        "q1": "Quick overview",
        "q4": "I like concise guidance and minimal AI interaction.",
        "q12": "Creativity is optional; efficiency is more important.",
        "q18": "I follow instructions carefully but avoid experimentation.",
        "q37": "I prefer observing and learning gradually.",
        "q42": "I adhere to rules with little personal adaptation."
    },
    # 8 - Flexible depending on task, adaptive style
    {
        "q1": "Hands-on experimentation",
        "q4": "I adjust my approach depending on the problem and context.",
        "q12": "Creativity is important when needed, otherwise I follow structure.",
        "q18": "I experiment or evaluate based on time constraints.",
        "q37": "I adapt my workflow rapidly to changing situations.",
        "q42": "I balance innovation and structure flexibly."
    },
    # 9 - Formal communication preference, methodical decision-making
    {
        "q1": "Structured",
        "q4": "I systematically analyze problems and implement step-by-step solutions.",
        "q12": "Creativity is useful for refining solutions.",
        "q18": "I carefully test AI suggestions and prioritize accuracy.",
        "q37": "I adapt methodically to ensure minimal mistakes.",
        "q42": "I integrate creativity cautiously within structured approaches."
    },
    # 10 - Playful / humorous preference, exploratory learning
    {
        "q1": "Explore examples yourself",
        "q4": "I experiment freely and enjoy playful approaches to problem-solving.",
        "q12": "Creativity drives my work; I prioritize it over strict rules.",
        "q18": "I test AI outputs in unconventional ways under time pressure.",
        "q37": "I adapt quickly and enjoy learning through experimentation.",
        "q42": "I combine humor and creativity within flexible structures."
    }
]

# Run summary engine for each set
summary_outputs = []

for idx, responses in enumerate(simulated_response_sets, 1):
    profile_summary = build_full_profile(example_profile, responses)
    summary_outputs.append({
        "test_id": idx,
        "simulated_answers": responses,
        "structured_profile": profile_summary['structured_profile'],
        "meta_inferences": profile_summary['meta_inferences'],
        "subtraits": profile_summary['subtraits'],
        "narrative": profile_summary['narrative']
    })

# Save JSON
with open("outputs/summary_engine_outputs_10.json", "w") as f:
    json.dump(summary_outputs, f, indent=2)

print("10 varied summary outputs saved for sandbox use.")