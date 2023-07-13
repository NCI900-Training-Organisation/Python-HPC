from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules=[
    Extension("search_max",
              ["search_max.pyx"],
              libraries=["m"],
              extra_compile_args = ["-fopenmp" ],
              extra_link_args=['-fopenmp']
              ) 
]

setup(
  name='search_max',
  ext_modules=ext_modules,
  cmdclass={'build_ext': build_ext},
)