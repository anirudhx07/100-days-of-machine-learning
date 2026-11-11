"""Day 001: Python Revision

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-04. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

def is_even(number: int) -> bool:
    return number % 2 == 0

def summarize_scores(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores cannot be empty")
    return {"count": len(scores), "total": sum(scores), "average": sum(scores) / len(scores)}

if __name__ == "__main__":
    scores = [78, 85, 91, 66]
    print("Even numbers:", [n for n in range(1, 11) if is_even(n)])
    print("Score summary:", summarize_scores(scores))
