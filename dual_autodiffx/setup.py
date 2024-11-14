"""Setup file for cython package alternative."""

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

# Define Cython extensions
extensions = [
    Extension(
        "dual_autodiff_x.dual",
        ["dual_autodiff_x/dual.pyx"],
        include_dirs=[np.get_include()],  # Include numpy headers if needed
    ),
    Extension(
        "dual_autodiff_x.autodiff",
        ["dual_autodiff_x/autodiff.pyx"],
        include_dirs=[np.get_include()],
    ),
]

# Setup configuration without versioning
setup(
    name="dual_autodiff_x",
    description="A Cythonized Python package for forward-mode automatic differentiation using dual numbers.",
    author="Lucas Curtin",
    author_email="lucas.curtin@gmail.com",
    packages=["dual_autodiff_x"],
    ext_modules=cythonize(extensions, language_level=3),
    zip_safe=False,  # Typically, Cython modules are not zip-safe
    include_dirs=[np.get_include()],
    install_requires=["numpy", "scipy"],
)
