# cython: profile=True

import random

cdef is_six(int ndice, int nsix):
    cdef int six = 0
    cdef int j
    for j in range(ndice):
        r = random.randint(1, 6)  # roll die no. j
        if r == 6:
            six += 1
    if six >= nsix:
        return 1
    return 0

def dice6_cy1(int N, int ndice, int nsix):
    cdef int M = 0            # no of successful events
    cdef double p
    for i in range(N):        # repeat N experiments
        M += is_six(ndice, nsix)
    p = float(M)/N
    return p