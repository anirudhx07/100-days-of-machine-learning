"""Day 086: Gradient Descent

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-28. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np
import matplotlib.pyplot as plt

def loss(w): return (w - 3) ** 2
def gradient(w): return 2 * (w - 3)

w = -4.0; learning_rate = 0.1; history = [w]
for _ in range(40):
    w -= learning_rate * gradient(w)
    history.append(w)
print("Final parameter:", round(w, 5), "loss:", round(loss(w), 8))
plt.plot(history, marker="o", markersize=3); plt.xlabel("Step"); plt.ylabel("Parameter w"); plt.title("Gradient descent trajectory"); plt.tight_layout(); plt.show()
