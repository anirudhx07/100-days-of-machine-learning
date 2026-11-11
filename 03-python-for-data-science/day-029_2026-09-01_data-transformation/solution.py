"""Day 029: Data Transformation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-01. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

df = pd.DataFrame({"date": ["2026-01-05", "2026-02-14", "2026-03-20"], "amount": [100, 250, 175]})
df["date"] = pd.to_datetime(df["date"], errors="raise")
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.day_name()
df["amount_log"] = (df["amount"] + 1).map(__import__("math").log)
print(df)
