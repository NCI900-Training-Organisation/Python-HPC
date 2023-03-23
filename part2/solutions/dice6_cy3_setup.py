from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules=[
    Extension("dice6_cy3",
              ["dice6_cy3.pyx"],
              libraries=["m"],
              extra_compile_args = ["-fopenmp" ],
              extra_link_args=['-fopenmp']
              ) 
]

setup(
  name='dice6_cy3',
  ext_modules=ext_modules,
  cmdclass={'build_ext': build_ext},
)