#cython: boundscheck=False, wraparound=False, nonecheck=False

from cython.parallel import prange

cdef extern from "<random>" namespace "std":
    # Pseudo-random number generator class
    cdef cppclass mt19937:
        mt19937() nogil 
        mt19937(unsigned int seed) nogil 
    
    # Uniform distribution class
    cdef cppclass uniform_real_distribution[T]:
        uniform_real_distribution() nogil
        uniform_real_distribution(T a, T b) nogil
        T operator()(mt19937 gen) nogil # Requires a randrandom number generator as argument
        

cdef int is_six(int id, int ndice, int nsix) nogil:
    cdef mt19937 gen = mt19937(id)
    cdef uniform_real_distribution[double] dist = uniform_real_distribution[double](0.0,1.0)

    cdef int r, j
    cdef int six = 0
    for j in range(ndice):
        r = 1 + <int>(dist(gen) * 6.0)
        if r == 6:
            six += 1

    if six >= nsix:
        return 1
    return 0


def dice6_cy4(int N, int ndice, int nsix):
    cdef int M = 0            # no of successful events
    cdef int i
    cdef double p

    for i in prange(N, nogil=True):
        M += is_six(i, ndice, nsix)

    p = (<float> M)/N

    return p