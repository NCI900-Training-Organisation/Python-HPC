#cython: boundscheck=False, wraparound=False, nonecheck=False
import numpy as np
from cython.parallel import prange
from libc.stdlib cimport rand, RAND_MAX

cdef int sample() nogil:
    cdef double x_ = rand()
    cdef double y_ = rand()
    cdef double x = x_ / RAND_MAX
    cdef double y = y_ / RAND_MAX

    if (x*x + y*y) <= 1:
        return 1
    else:
        return 0

def sample_parallel(nsamples):
    cdef int N = nsamples
    cdef double[:] X = np.zeros(nsamples)
    cdef int i
    cdef double x_, y_, x, y

    for i in prange(N, nogil=True, num_threads=1):
        x_ = rand()
        y_ = rand()
        x = x_ / RAND_MAX
        y = y_ / RAND_MAX
        if (x*x + y*y) <= 1:
            X[i] = 1
        else:
            X[i] = 0
    return np.sum(X)