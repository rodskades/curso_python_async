"""
Preparando o build a ser feito com:

python setup.py build_ext --inplace
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['cumprimenta.pyx', 'computa.pyx'])
)
