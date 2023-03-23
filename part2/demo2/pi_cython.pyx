from pi_cython cimport sample

def cy_serial_sampler(n):
    cdef int i
    cdef int count = 0
    for i in range(n):
        count += sample()
    return count