from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# TODO: 
# write an Extension object for dice6_cy2.pyx and implement the setup() function.
# NOTE: You will need to link openMP and potentially the math library m.