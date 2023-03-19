# distutils: language=c++

from pi_cython_h cimport sample_serial


def serial_sampler(n):
    cdef int nsamples = n
    return sample_serial(nsamples)
