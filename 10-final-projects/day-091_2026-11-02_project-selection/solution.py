"""Day 091: Project Selection

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-02. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

projects = {
    "AQI forecasting": {"impact": 5, "feasibility": 4, "data_access": 4, "evaluation": 5},
    "Movie recommender": {"impact": 3, "feasibility": 4, "data_access": 5, "evaluation": 3},
    "Plant disease classifier": {"impact": 4, "feasibility": 3, "data_access": 3, "evaluation": 5},
}
weights = {"impact": 0.30, "feasibility": 0.25, "data_access": 0.25, "evaluation": 0.20}
for name, scores in projects.items():
    total = sum(scores[key] * weights[key] for key in weights)
    print(f"{name}: {total:.2f}/5")
