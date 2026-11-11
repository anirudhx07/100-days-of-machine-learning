"""Day 015: Statistics

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-18. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import statistics as stats

data = [12, 15, 14, 10, 19, 15, 13]
print("Count:", len(data))
print("Mean:", stats.mean(data))
print("Median:", stats.median(data))
print("Population std dev:", stats.pstdev(data))
print("Sample std dev:", stats.stdev(data))
