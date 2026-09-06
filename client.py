"""
Multi-Criteria Evaluation Rubric and Actionable Critique Synthesizer.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional

class CritiqueRubricEvaluatorClient:
    """
    Evaluates LLM generation drafts against multi-dimensional rubrics:
    - Factual accuracy & groundedness
    - Conciseness & brevity
    - Formatting compliance
    - Actionability & clarity
    Synthesizes targeted refinement directives.
    """

    def __init__(self):
        pass

    def evaluate_draft(self, text: str, criteria: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Evaluates text against criteria dictionary:
        { "criterion_name": { "weight": float, "min_words": int, "must_contain": List[str] } }
        """
        scores = {}
        critiques = []
        words = text.split()
        word_count = len(words)

        total_weighted_score = 0.0
        total_weight = 0.0

        for crit_name, crit_spec in criteria.items():
            weight = crit_spec.get("weight", 1.0)
            total_weight += weight
            crit_score = 100.0

            # Check min words
            min_words = crit_spec.get("min_words", 0)
            if word_count < min_words:
                crit_score -= 30.0
                critiques.append(f"[{crit_name}] Too brief: {word_count} words (minimum {min_words}).")

            # Check required keywords
            for kw in crit_spec.get("must_contain", []):
                if kw.lower() not in text.lower():
                    crit_score -= 20.0
                    critiques.append(f"[{crit_name}] Missing required concept: '{kw}'.")

            crit_score = max(0.0, crit_score)
            scores[crit_name] = crit_score
            total_weighted_score += crit_score * weight

        overall_score = round(total_weighted_score / total_weight, 2) if total_weight > 0 else 0.0

        return {
            "overall_score": overall_score,
            "status": "PASS" if overall_score >= 80.0 else "NEEDS_REFINEMENT",
            "criterion_scores": scores,
            "critique_points": critiques,
            "word_count": word_count
        }
