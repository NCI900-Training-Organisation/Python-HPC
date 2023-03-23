from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(name = "pi_cython",
             language='c++',
             extra_compile_args=['-std=c++17'],
             sources=["pi_cython.pyx"]
    )
]

setup(
    name="pi_cython",
    ext_modules=ext_modules,
    cmdclass = {'build_ext': build_ext},
)