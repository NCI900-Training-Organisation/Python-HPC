from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("dice6_cy4",
              ["dice6_cy4.pyx"],
              libraries=["m"],
              language='c++',
              extra_compile_args = ["-fopenmp" ],
              extra_link_args=['-fopenmp', '-std=c++11']
              ) 
]

setup(
  name='dice6_cy4',
  ext_modules=ext_modules,
  cmdclass={'build_ext': build_ext},
)
