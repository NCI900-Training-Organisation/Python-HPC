from libc.stdio cimport printf

cdef int a_global_variable

def function():
    cdef double x = 5.0
    cdef char c = 'y'
    cdef unsigned long z = -1
    printf("%c", c)
    return x, c, z

