#cython: boundscheck=False, wraparound=False, nonecheck=False

from libc.stdlib cimport rand, RAND_MAX
from cython.parallel import prange
import  numpy as np
# cimport numpy as np
import cython


cdef int is_six(int ndice, int nsix) nogil:
    cdef int r, j
    cdef int six = 0
    for j in range(ndice):
        r = 1 + <int>((rand() * 6.0) / RAND_MAX)
        if r == 6:
            six += 1

    if six >= nsix:
        return 1
    return 0


def dice6_cy3(int N, int ndice, int nsix):
    cdef int M = 0            # no of successful events
    cdef int i
    cdef double p

    for i in prange(N, nogil=True):
        M += is_six(ndice, nsix)

    p = (<float> M)/N

    return p
