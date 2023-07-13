#cython: boundscheck=False, wraparound=False, nonecheck=False

from libc.stdlib cimport rand, RAND_MAX
from posix.unistd cimport sleep

from cython.parallel import prange
import  numpy as np
import cython



cdef struct A:
    double a

def search_max(double[::1] vals):
    cdef A max_val = [-1.0]
    cdef int i
    cdef int n = len(vals)
    for i in prange(n, nogil=True, num_threads=100):
        # sleep(<int>((rand()*1.0) / RAND_MAX))
        if(vals[i]>max_val.a):
            max_val.a = vals[i]
    return max_val.a

