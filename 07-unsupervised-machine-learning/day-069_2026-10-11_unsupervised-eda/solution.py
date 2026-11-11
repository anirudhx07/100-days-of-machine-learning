"""Day 069: Unsupervised EDA

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-11. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = load_iris(as_frame=True)
df = data.frame.copy()
features = list(data.feature_names)
X = StandardScaler().fit_transform(df[features])
df["cluster"] = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)
print(df.groupby("cluster")[features].mean().round(2))
sns.pairplot(df, vars=features[:3], hue="cluster", corner=True)
plt.show()
