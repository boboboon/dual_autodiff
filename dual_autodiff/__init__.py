"""Our package for automatic dual differentiation."""

# dual_autodiff/__init__.py
from .dual import Dual
from .version import __version__  # Import the version from version.py

__all__ = ["Dual", "__version__"]
