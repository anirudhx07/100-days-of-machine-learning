"""Day 046: Feature Engineering

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-18. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

df = pd.DataFrame({"date": pd.to_datetime(["2026-01-01", "2026-01-03", "2026-02-10"]), "quantity": [2, 5, 3], "unit_price": [100, 80, 120]})
df["revenue"] = df["quantity"] * df["unit_price"]
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"] >= 5
print(df)
