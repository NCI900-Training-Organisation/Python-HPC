from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(name="demo4",
              sources=['demo4.pyx'],
    )
]

setup(
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
)