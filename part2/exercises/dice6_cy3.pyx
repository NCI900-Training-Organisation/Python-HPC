#cython: boundscheck=False, wraparound=False, nonecheck=False

from libc.stdlib cimport rand, RAND_MAX
from cython.parallel import prange
import  numpy as np
import cython


cdef int is_six(int ndice, int nsix) nogil:
    # TODO


def dice6_cy3(int N, int ndice, int nsix):
    # TODO
