"""Day 019: Distributions

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-22. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

rng = np.random.default_rng(7)
samples = rng.normal(loc=50, scale=10, size=5_000)
print("Empirical mean:", round(float(samples.mean()), 2))
print("Empirical standard deviation:", round(float(samples.std()), 2))
print("10th, 50th, 90th percentiles:", np.percentile(samples, [10, 50, 90]))
