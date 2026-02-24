from typing import Dict
import numpy as np
import json

# ---------------------------
# Embedding & similarity
# ---------------------------
def embed_text(text: str) -> np.ndarray:
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(512)

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

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

# ---------------------------
# Core engine functions
# ---------------------------
def analyze_free_text_semantic(responses: Dict[str, str]) -> Dict[str, str]:
    """
    Analyzes semantic meaning of free-text responses and extracts insights.

    Args:
        responses (Dict[str, str]): A dictionary mapping question identifiers to user free-text responses.

    Returns:
        Dict[str, str]: A dictionary of insights based on the semantic proximity of responses
        to predefined categories. Example keys include 'learning_style', 'creativity_preference'.
    """
    insights: Dict[str, str] = {}
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

def analyze_subtraits(responses: Dict[str, str]) -> Dict[str, Dict[str, float | str]]:
    """
    Extracts raw numerical or string sub-traits from free text based on keyword matches.

    Args:
        responses (Dict[str, str]): A dictionary mapping question identifiers to user free-text responses.

    Returns:
        Dict[str, Dict[str, float | str]]: A structured dictionary of inferred sub-traits and their
        calculated values (from 0.0 to 1.0 or qualitative labels).
    """
    subtraits: Dict[str, Dict[str, float | str]] = {
        "learning": {}, "decision_making": {}, "creativity": {},
        "communication": {}, "collaboration": {}, "ethics": {},
        "motivation": {}, "personality": {}
    }
    for key, text in responses.items():
        text_lower = text.lower()
        subtraits["learning"]["depth_vs_breadth"] = 0.9 if "detailed" in text_lower else 0.4
        subtraits["learning"]["analytical_vs_intuitive"] = 0.8 if "analyze" in text_lower else 0.5
        subtraits["decision_making"]["risk_tolerance"] = 0.8 if "risk" in text_lower or "experiment" in text_lower else 0.3
        subtraits["decision_making"]["ambiguity_tolerance"] = 0.9 if "uncertain" in text_lower or "flexible" in text_lower else 0.5
        subtraits["creativity"]["originality"] = 0.9 if "creative" in text_lower or "innovative" in text_lower else 0.4
        subtraits["creativity"]["procedural_thinking"] = 0.7 if "step-by-step" in text_lower else 0.5
        subtraits["communication"]["formality"] = 0.8 if "formal" in text_lower else 0.5
        subtraits["communication"]["empathy"] = 0.9 if "empathetic" in text_lower or "considerate" in text_lower else 0.5
        subtraits["communication"]["humor"] = 0.7 if "humor" in text_lower or "joke" in text_lower else 0.2
        subtraits["collaboration"]["preference"] = "co-creative" if "together" in text_lower or "co-create" in text_lower else "solo"
        subtraits["collaboration"]["patience"] = 0.9 if "step-by-step" in text_lower or "detailed" in text_lower else 0.5
        subtraits["ethics"]["moral_rigidity"] = 0.9 if "ethics" in text_lower or "honest" in text_lower else 0.5
        subtraits["ethics"]["fairness_orientation"] = 0.8 if "fair" in text_lower else 0.5
        subtraits["motivation"]["curiosity_drive"] = 0.9 if "explore" in text_lower or "curious" in text_lower else 0.4
        subtraits["motivation"]["achievement_focus"] = 0.8 if "goal" in text_lower or "solve" in text_lower else 0.5
        subtraits["personality"]["openness"] = 0.9 if "try new" in text_lower or "open-minded" in text_lower else 0.5
        subtraits["personality"]["conscientiousness"] = 0.8 if "organized" in text_lower or "methodical" in text_lower else 0.5
        subtraits["personality"]["adaptability"] = 0.85 if "flexible" in text_lower else 0.5
    return subtraits

def generate_meta_inferences(profile: Dict[str, str], free_text_insights: Dict[str, str]) -> Dict[str, str]:
    """
    Synthesizes structured profile data and free-text insights to generate higher-level
    meta-inferences about the user's personality and preferences.

    Args:
        profile (Dict[str, str]): The user's structured profile or preferences.
        free_text_insights (Dict[str, str]): Key-value insights generated via semantic analysis.

    Returns:
        Dict[str, str]: A dictionary containing high-level inferences like preferred approach to
        problem solving and learning.
    """
    meta: Dict[str, str] = {}
    if profile.get("patience_level") in ["High", "Medium"]:
        meta["learning_style"] = "Prefers detailed, step-by-step guidance"
    else:
        meta["learning_style"] = "Prefers concise, exploratory learning"
    if profile.get("creativity_level") in ["High", "Very high"] and profile.get("risk_tolerance") in ["High", "Moderate"]:
        meta["approach_to_problem"] = "Leans toward innovative, experimental solutions"
    else:
        meta["approach_to_problem"] = "Prefers structured, methodical solutions"
    if profile.get("collaboration_preference") in ["Co-creative", "Open-ended"]:
        meta["collaboration_style"] = "Enjoys interactive, collaborative AI interactions"
    else:
        meta["collaboration_style"] = "Prefers guided or self-directed AI interactions"
    meta["ethics_focus"] = "Strongly guided by ethical preferences" if profile.get("ethical_priorities") else "Flexible ethical stance"
    meta.update(free_text_insights)
    return meta

def build_full_profile(profile: Dict[str, str], free_text_responses: Dict[str, str]) -> Dict[str, object]:
    """
    Constructs a complete AI personality profile based on quantitative profile parameters
    and qualitative free-text responses.

    Args:
        profile (Dict[str, str]): Initial user profile parameters.
        free_text_responses (Dict[str, str]): User-provided qualitative text answers.

    Returns:
        Dict[str, object]: A comprehensive profile containing the structured elements,
        sub-traits, meta-inferences, and a synthesized narrative overview.
    """
    free_text_insights = analyze_free_text_semantic(free_text_responses)
    subtraits = analyze_subtraits(free_text_responses)
    meta = generate_meta_inferences(profile, free_text_insights)
    narrative_lines = [
        f"The user intends to work with {profile.get('model_preference')}.",
        f"Meta-inferences: {meta}.",
        f"Sub-traits extracted from responses: {subtraits}."
    ]
    narrative = "\n".join(narrative_lines)
    return {
        "structured_profile": profile,
        "meta_inferences": meta,
        "subtraits": subtraits,
        "narrative": narrative
    }
