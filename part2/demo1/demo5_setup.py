from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("demo5",
              ["demo5.pyx"],
              libraries=["m"],
              extra_compile_args = ["-fopenmp" ],
              extra_link_args=['-fopenmp']
              ) 
]

setup(
  ext_modules=ext_modules,
  cmdclass={'build_ext': build_ext},
)
