# Usage

## Basic Example with the Dual Class

The `Dual` class represents a dual number with real and dual parts for automatic differentiation.

```python
from dual_autodiff import Dual

# Initialize a dual number with real part 2.0 and dual part 1.0
x = Dual(2.0, 1.0)

# Perform operations on the dual number
y = x ** 2  # Computes x^2 using the Dual class
print(y)  # Expected output: Dual(real=4.0, dual=4.0)
The real part of the result is the function's value, while the dual part is the derivative.

Using the differentiate Function

The differentiate function computes the derivative of a function at a specific point.

from dual_autodiff.autodiff_tools import differentiate

# Define a function for differentiation
def func(x):
    return x ** 2 + 3 * x

# Compute the derivative at x=3
derivative_at_3 = differentiate(func, 3.0)
print(derivative_at_3)  # Expected output: derivative value at x=3
This function initializes a dual number with a dual component of 1 to propagate derivative information through the computation.