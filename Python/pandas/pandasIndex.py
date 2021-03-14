import numpy as np
import pandas as pd

# Index Object
idx = pd.Index([2, 4, 6, 8, 10])
idx
idx[1]
idx[0:4:2]
idx[-1::]
idx[::2]
print(idx)
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)

# 21m25s
