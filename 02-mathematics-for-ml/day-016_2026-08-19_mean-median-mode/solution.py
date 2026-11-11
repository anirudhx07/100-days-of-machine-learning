"""Day 016: Mean Median Mode

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-19. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from statistics import mean, median, multimode

data = [10, 12, 12, 13, 15, 100]
print("Mean:", mean(data))
print("Median:", median(data))
print("Mode(s):", multimode(data))
print("Sorted:", sorted(data))
