"""Day 087: Tensorflow Pytorch

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-29. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

try:
    import torch
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    print("PyTorch:", torch.__version__)
    print("Tensor:\n", x)
    print("Mean:", x.mean().item())
    print("Requires grad example:", torch.tensor(2.0, requires_grad=True))
except ImportError:
    import numpy as np
    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    print("PyTorch is not installed. NumPy fallback mean:", x.mean())
    print("To try PyTorch, install it using the official selector at https://pytorch.org/get-started/locally/")
