"""Day 004: Conditionals

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-07. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

def grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "Fail"

for score in [95, 82, 64, 42, 75, 60]:
    print(score, "->", grade(score))
