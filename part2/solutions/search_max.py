import numpy as np
from search_max import search_max

A = np.random.rand(1000)

print(search_max(A) - search_max(A))

