from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("cy_psample",
              ["cy_psample.pyx"],
              libraries=["m"],
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp" ],
              extra_link_args=['-fopenmp']
              ) 
]

setup( 
  name = "cy_psample",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules
)
