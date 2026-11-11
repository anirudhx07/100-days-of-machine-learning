"""Day 030: Data Aggregation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-02. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

sales = pd.DataFrame({"region": ["North", "South", "North", "West", "South"], "revenue": [1200, 900, 800, 1500, 1100], "orders": [4, 3, 2, 5, 4]})
summary = sales.groupby("region").agg(total_revenue=("revenue", "sum"), orders=("orders", "sum"), average_order_value=("revenue", "mean"))
print(summary.sort_values("total_revenue", ascending=False))
