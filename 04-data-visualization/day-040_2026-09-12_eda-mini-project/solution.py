"""Day 040: EDA Mini Project

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-12. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame.copy()
df["species"] = df["target"].map(dict(enumerate(data.target_names)))
print(df.groupby("species")["petal length (cm)"].agg(["count", "mean", "median", "std"]))
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(data=df, x="petal length (cm)", hue="species", kde=True, ax=axes[0])
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", ax=axes[1])
fig.tight_layout()
plt.show()
