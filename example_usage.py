"""
Demonstration of genpark-critique-rubric-multi-criteria-evaluator-skill
"""

from client import CritiqueRubricEvaluatorClient

def main():
    evaluator = CritiqueRubricEvaluatorClient()

    rubric = {
        "depth": {"weight": 1.5, "min_words": 15},
        "terminology": {"weight": 1.0, "must_contain": ["latency", "throughput"]}
    }

    draft = "We optimized the database queries, significantly reducing network latency."

    report = evaluator.evaluate_draft(draft, rubric)
    print("=== RUBRIC CRITIQUE REPORT ===")
    print("Overall Score:", report["overall_score"])
    print("Status:", report["status"])
    print("Criterion Scores:", report["criterion_scores"])
    print("Critique Points:")
    for c in report["critique_points"]:
        print(" -", c)

if __name__ == "__main__":
    main()
