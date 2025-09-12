from typing import Dict
import numpy as np

# ---------------------------
# Step 1: Semantic Embeddings
# ---------------------------
def embed_text(text: str) -> np.ndarray:
    """Placeholder embedding function. Replace with real embeddings in production."""
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(512)

INSIGHT_CATEGORIES = {
    "learning_style_detailed": embed_text("Prefers detailed, structured step-by-step guidance"),
    "learning_style_exploratory": embed_text("Prefers concise, exploratory learning"),
    "creativity_high": embed_text("Leans toward creative, innovative, exploratory approaches"),
    "creativity_low": embed_text("Prefers structured, methodical approaches"),
    "risk_high": embed_text("Comfortable with high risk and uncertainty"),
    "risk_low": embed_text("Prefers safe, low-risk approaches"),
    "collaboration_co": embed_text("Prefers collaborative, co-creative interactions with AI"),
    "collaboration_solo": embed_text("Prefers guided or self-directed interactions with AI"),
    "tone_formal": embed_text("Prefers formal, serious, professional tone"),
    "tone_informal": embed_text("Prefers informal, casual tone"),
    "ethics_strong": embed_text("Strong ethical orientation, fairness and honesty prioritized"),
    "ethics_flexible": embed_text("Flexible ethical stance, pragmatic when needed")
}

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# ---------------------------
# Step 2: Semantic Free-Text Analysis
# ---------------------------
def analyze_free_text_semantic(responses: Dict[str, str]) -> Dict:
    insights = {}
    for key, text in responses.items():
        text_vec = embed_text(text)
        best_match = None
        best_score = -1
        for category, cat_vec in INSIGHT_CATEGORIES.items():
            score = cosine_similarity(text_vec, cat_vec)
            if score > best_score:
                best_score = score
                best_match = category
        if best_match.startswith("learning_style"):
            insights["learning_style"] = "Prefers detailed guidance" if "detailed" in best_match else "Prefers exploratory guidance"
        elif best_match.startswith("creativity"):
            insights["creativity_preference"] = "High creativity" if "high" in best_match else "Structured approach"
        elif best_match.startswith("risk"):
            insights["risk_behavior"] = "High risk tolerance" if "high" in best_match else "Low risk tolerance"
        elif best_match.startswith("collaboration"):
            insights["collaboration_style"] = "Collaborative" if "co" in best_match else "Solo / guided"
        elif best_match.startswith("tone"):
            insights["tone_preference"] = "Formal" if "formal" in best_match else "Informal"
        elif best_match.startswith("ethics"):
            insights["ethics_focus"] = "Strong ethical focus" if "strong" in best_match else "Flexible ethics"
    return insights

# ---------------------------
# Step 3: Sub-Trait Extraction
# ---------------------------
def analyze_subtraits(responses: Dict[str, str]) -> Dict[str, Dict]:
    subtraits = {
        "learning": {},
        "decision_making": {},
        "creativity": {},
        "communication": {},
        "collaboration": {},
        "ethics": {},
        "motivation": {},
        "personality": {}
    }
    for key, text in responses.items():
        text_lower = text.lower()
        # Learning
        subtraits["learning"]["depth_vs_breadth"] = 0.9 if "detailed" in text_lower else 0.4
        subtraits["learning"]["analytical_vs_intuitive"] = 0.8 if "analyze" in text_lower else 0.5
        # Decision-Making / Risk
        subtraits["decision_making"]["risk_tolerance"] = 0.8 if "risk" in text_lower or "experiment" in text_lower else 0.3
        subtraits["decision_making"]["ambiguity_tolerance"] = 0.9 if "uncertain" in text_lower or "flexible" in text_lower else 0.5
        # Creativity
        subtraits["creativity"]["originality"] = 0.9 if "creative" in text_lower or "innovative" in text_lower else 0.4
        subtraits["creativity"]["procedural_thinking"] = 0.7 if "step-by-step" in text_lower else 0.5
        # Communication
        subtraits["communication"]["formality"] = 0.8 if "formal" in text_lower else 0.5
        subtraits["communication"]["empathy"] = 0.9 if "empathetic" in text_lower or "considerate" in text_lower else 0.5
        subtraits["communication"]["humor"] = 0.7 if "humor" in text_lower or "joke" in text_lower else 0.2
        # Collaboration
        subtraits["collaboration"]["preference"] = "co-creative" if "together" in text_lower or "co-create" in text_lower else "solo"
        subtraits["collaboration"]["patience"] = 0.9 if "step-by-step" in text_lower or "detailed" in text_lower else 0.5
        # Ethics
        subtraits["ethics"]["moral_rigidity"] = 0.9 if "ethics" in text_lower or "honest" in text_lower else 0.5
        subtraits["ethics"]["fairness_orientation"] = 0.8 if "fair" in text_lower else 0.5
        # Motivation
        subtraits["motivation"]["curiosity_drive"] = 0.9 if "explore" in text_lower or "curious" in text_lower else 0.4
        subtraits["motivation"]["achievement_focus"] = 0.8 if "goal" in text_lower or "solve" in text_lower else 0.5
        # Personality
        subtraits["personality"]["openness"] = 0.9 if "try new" in text_lower or "open-minded" in text_lower else 0.5
        subtraits["personality"]["conscientiousness"] = 0.8 if "organized" in text_lower or "methodical" in text_lower else 0.5
        subtraits["personality"]["adaptability"] = 0.85 if "flexible" in text_lower else 0.5
    return subtraits

# ---------------------------
# Step 4: Meta-Inference Generator
# ---------------------------
def generate_meta_inferences(profile: Dict, free_text_insights: Dict) -> Dict:
    meta = {}
    # Learning style
    if profile.get("patience_level") in ["High", "Medium"]:
        meta["learning_style"] = "Prefers detailed, step-by-step guidance"
    else:
        meta["learning_style"] = "Prefers concise, exploratory learning"
    # Creativity vs risk
    if profile.get("creativity_level") in ["High", "Very high"] and profile.get("risk_tolerance") in ["High", "Moderate"]:
        meta["approach_to_problem"] = "Leans toward innovative, experimental solutions"
    else:
        meta["approach_to_problem"] = "Prefers structured, methodical solutions"
    # Collaboration
    if profile.get("collaboration_preference") in ["Co-creative", "Open-ended"]:
        meta["engagement_style"] = "Enjoys interactive, collaborative AI interactions"
    else:
        meta["engagement_style"] = "Prefers guided or self-directed AI interactions"
    # Ethics
    meta["ethics_focus"] = "Strongly guided by ethical preferences" if profile.get("ethical_priorities") else "Flexible ethical stance"
    # Merge free-text insights
    meta.update(free_text_insights)
    return meta

# ---------------------------
# Step 5: Build Full Profile Summary
# ---------------------------
def build_full_profile(profile: Dict, free_text_responses: Dict) -> Dict:
    free_text_insights = analyze_free_text_semantic(free_text_responses)
    subtraits = analyze_subtraits(free_text_responses)
    meta = generate_meta_inferences(profile, free_text_insights)

    narrative = (
        f"The user intends to work with {profile.get('model_preference')}. "
        f"Meta-inferences: {meta}. "
        f"Sub-traits extracted from responses: {subtraits}."
    )

    return {
        "structured_profile": profile,
        "meta_inferences": meta,
        "subtraits": subtraits,
        "narrative": narrative
    }

# ---------------------------
# Step 6: System Prompt Generator
# ---------------------------
def generate_system_prompt(profile_summary: Dict) -> str:
    narrative = profile_summary['narrative']
    prompt = (
        "You are an expert AI assistant. Use the following user profile to guide all interactions:\n\n"
        f"{narrative}\n\n"
        "Instructions for outputs:\n"
        "- Match tone, formality, and communication style.\n"
        "- Respect risk tolerance, learning style, and ethical priorities.\n"
        "- Engage collaboratively according to engagement style.\n"
        "- Provide guidance aligned with creativity, decision-making, and sub-traits.\n"
        "- Maximize usefulness, clarity, and alignment with the user's objectives."
    )
    return prompt

# ---------------------------
# Demo Execution
# ---------------------------
if __name__ == "__main__":
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

    free_text_responses = {
        "q4": "I prefer structured step-by-step guidance but like occasional creative suggestions.",
        "q12": "I enjoy tasks where creativity is key, especially when brainstorming solutions.",
        "q18": "I would test AI suggestions but rely on my judgment when deadlines are tight."
    }

    profile_summary = build_full_profile(example_profile, free_text_responses)
    system_prompt = generate_system_prompt(profile_summary)

    print("\n--- Structured Profile ---")
    print(profile_summary['structured_profile'])
    print("\n--- Meta Inferences ---")
    print(profile_summary['meta_inferences'])
    print("\n--- Sub-Traits ---")
    print(profile_summary['subtraits'])
    print("\n--- Narrative ---")
    print(profile_summary['narrative'])
    print("\n--- Generated System Prompt ---")
    print(system_prompt)
