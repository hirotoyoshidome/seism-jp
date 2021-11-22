from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


source = [
    "./sample.pyx",
    # "sample.cpp",
]

setup(
    cmdclass=dict(build_ext=build_ext),
    ext_modules=[
        Extension("mycalc", source, language="c++"),
    ],
)
