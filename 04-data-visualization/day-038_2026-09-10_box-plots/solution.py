"""Day 038: Box Plots

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-10. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({"day": ["Mon", "Mon", "Tue", "Tue", "Wed", "Wed", "Thu", "Thu"], "bill": [12, 18, 21, 17, 31, 27, 15, 24]})
fig, ax = plt.subplots()
sns.boxplot(data=df, x="day", y="bill", ax=ax)
ax.set(title="Example bill distribution by day", xlabel="Day", ylabel="Bill")
fig.tight_layout()
plt.show()
