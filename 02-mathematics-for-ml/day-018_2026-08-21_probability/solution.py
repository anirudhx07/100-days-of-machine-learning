"""Day 018: Probability

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-21. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

rng = np.random.default_rng(42)
flips = rng.choice([0, 1], size=10_000)  # 1 represents heads
heads = int(flips.sum())
print("Heads:", heads)
print("Empirical P(heads):", heads / len(flips))
print("Theoretical P(heads):", 0.5)
