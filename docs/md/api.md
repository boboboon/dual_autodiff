 API Documentation

## The Dual Class

The `Dual` class supports arithmetic operations and elementary functions on dual numbers for automatic differentiation. Key methods include:

- `__add__`: Adds two dual numbers or a dual number and a float.
- `__sub__`: Subtracts a dual number or a float.
- `__mul__`: Multiplies by another dual number or a float.
- `__truediv__`: Divides by another dual number or a float.
- `sin()`: Computes the sine of a dual number.
- `cos()`: Computes the cosine of a dual number.
- `exp()`: Computes the exponential function.
- `log()`: Computes the natural logarithm (raises a `ValueError` for non-positive inputs).

## differentiate Function

The `differentiate` function calculates the derivative of a function at a specified point by initializing a dual number with a dual component of 1, allowing derivatives to propagate through the function.