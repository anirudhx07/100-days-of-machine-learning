"""Day 083: Activation Functions

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-25. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 300)
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)
plt.plot(x, sigmoid, label="sigmoid")
plt.plot(x, tanh, label="tanh")
plt.plot(x, relu, label="ReLU")
plt.ylim(-1.2, 6.2); plt.grid(alpha=0.3); plt.legend(); plt.title("Activation functions"); plt.tight_layout(); plt.show()
