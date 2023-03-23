from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(name="helloworld",
              sources=['helloworld.pyx'],
    )
]

setup(
    ext_modules = [Extension('helloworld', ['helloworld.pyx'],)],
    cmdclass = {'build_ext': build_ext},
)