"""Day 048: Encoding

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-20. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

categories = pd.DataFrame({"city": ["Agra", "Delhi", "Noida", "Agra"]})
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
encoded = encoder.fit_transform(categories[["city"]])
print("Categories:", encoder.categories_)
print(pd.DataFrame(encoded, columns=encoder.get_feature_names_out(["city"])))
