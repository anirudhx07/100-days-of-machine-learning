"""Day 025: Pandas Basics

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-28. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

scores = pd.Series([82, 91, 76], index=["Asha", "Kabir", "Mira"], name="score")
print(scores)
print("Kabir by label:", scores.loc["Kabir"])
print("First value by position:", scores.iloc[0])
print("Average:", scores.mean())
