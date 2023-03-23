from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name='dice6_cy1',
  ext_modules=[Extension('dice6_cy1', ['dice6_cy1.pyx'],)],
  cmdclass={'build_ext': build_ext},
)