"""Our package for automatic dual differentiation with Cython."""

from .autodiff import differentiate
from .dual import Dual

__all__ = ["Dual", "differentiate"]
