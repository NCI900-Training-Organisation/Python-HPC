from libc.math cimport sin


cdef double f(double x):
    return sin(x * x)

def sin_squared(x):
    return f(x)

