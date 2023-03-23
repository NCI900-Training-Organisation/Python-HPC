from libc.stdlib cimport rand, RAND_MAX

cdef is_six(int ndice, int nsix):
    cdef int six = 0
    cdef int j, r
    for j in range(ndice):
        # Roll die no. j
        r = 1 + int((rand()*6.0)/(RAND_MAX))
        if r == 6:
            six += 1
    if six >= nsix:       # successful event?
        return 1
    return 0


def dice6_cy2(int N, int ndice, int nsix):
    cdef int M = 0            # no of successful events
    cdef double p
    for i in range(N):
        M += is_six(ndice, nsix)
    p = float(M)/N
    return p
