from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


source = ['./sample.pyx']

setup(
    cmdclass = dict(build_ext = build_ext),
    ext_modules = [
        Extension('sample_add', source, language='c++')
    ]
)
