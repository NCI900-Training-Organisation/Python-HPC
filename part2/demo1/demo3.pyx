cdef int mix_func(x):
    cdef int y = 5+x
    return y

cdef int c_func(int x):
    cdef int y = 5+x
    return y

def func(y):
    return c_func(y)