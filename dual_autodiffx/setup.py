from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy

# Define the extensions for Cython compilation
extensions = [
    Extension(
        "dual_autodiffx.dual",
        ["dual_autodiffx/dual.pyx"],  # Correct path for dual.pyx
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    ),
    Extension(
        "dual_autodiffx.autodiff",
        ["dual_autodiffx/autodiff.pyx"],  # Correct path for autodiff.pyx
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    ),
]

# Setup configuration
setup(
    name="dual_autodiffx",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=cythonize(
        extensions,
        language_level="3",
        compiler_directives={
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
        },
    ),
    zip_safe=False,
)
