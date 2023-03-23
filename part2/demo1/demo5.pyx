from cython.parallel cimport prange
from libc.math cimport sin

cdef double sin_squared(int x) nogil:
    return sin(x*x)
    
cdef int i
cdef double X[200] 
for i in prange(200, nogil=True):
    X[i] = sin_squared(i)