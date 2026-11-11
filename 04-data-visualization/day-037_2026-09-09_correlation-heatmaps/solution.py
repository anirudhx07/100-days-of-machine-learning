"""Day 037: Correlation Heatmaps

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-09. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

df = load_iris(as_frame=True).frame
numeric = df.select_dtypes(include="number").drop(columns=["target"])
corr = numeric.corr()
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("Iris numeric-feature correlation")
fig.tight_layout()
plt.show()
