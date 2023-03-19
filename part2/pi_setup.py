from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

os.environ["CC"] = "g++"

extensions = [
    Extension(name = "pi_cython",
             language='c++',
             extra_compile_args=['-std=c++17'],
             sources=["pi_cython.pyx"],
             undef_macros=["NDEBUG"]
    )
]

setup(
    ext_modules=cythonize(
        extensions, language_level=3, annotate=False
    )
)