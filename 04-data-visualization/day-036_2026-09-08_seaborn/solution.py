"""Day 036: Seaborn

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-08. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({"bill": [12, 18, 24, 31, 15, 27, 35, 21], "tip": [2, 3, 4, 5, 2.5, 4.5, 6, 3.5], "meal": ["Lunch", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Dinner", "Lunch"]})
fig, ax = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=df, x="bill", y="tip", hue="meal", ax=ax)
ax.set(title="Example tip versus bill, grouped by meal")
fig.tight_layout()
plt.show()
