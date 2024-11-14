.. Welcome to dual_autodiff's documentation!
.. =======================================

dual_autodiff is a Python package for forward-mode automatic differentiation using dual numbers.

Contents:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   contributing

Installation
============

To install dual_autodiff, simply use pip:

pip install -e .


This will install the package in editable mode, which is useful for development. It allows you to make changes to the code and have them reflected without reinstalling.

Usage
=====

Here, you can describe how to use the package with code examples.

For example, you can create a `Dual` number and perform operations on it:

```python
from dual_autodiff import Dual

x = Dual(2.0, 1.0)
y = x ** 2
print(y)  # You can describe the output here