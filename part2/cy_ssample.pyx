import numpy as np

def sample():
    x = np.random.rand()
    y = np.random.rand()

    if (x*x + y*y) <= 1:
        return 1
    else:
        return 0

def sample_serial(nsamples):
    count = 0
    for i in range(nsamples):
        count += sample()
    return count