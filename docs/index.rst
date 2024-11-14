# Welcome to dual_autodiff’s Documentation!

**dual_autodiff** is a Python package for forward-mode automatic differentiation using dual numbers. This documentation covers the theoretical background, installation instructions, usage examples, API reference, and contributing guidelines for developers.

**Contents:**

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Analytical Solutions and Test Cases](#analytical-solutions-and-test-cases)
- [Contributing](#contributing)

---

## Overview

The **dual_autodiff** library leverages dual numbers to enable forward-mode automatic differentiation, a powerful technique for symbolic differentiation. This is particularly useful for applications requiring precise and efficient derivative computations, such as optimisation, machine learning, and scientific computing.

### Dual Numbers and Automatic Differentiation

Dual numbers are an extension of real numbers designed to compute derivatives through symbolic propagation. A dual number is expressed as:

$$
x = a + b \epsilon
$$

where:

- **a** is the real part,
- **b** is the dual part, representing the derivative, and
- **ε** is an infinitesimal element with the property: $\epsilon^2 = 0$.

By defining operations on dual numbers, such as addition, multiplication, and elementary functions (e.g., `sin`, `cos`, `exp`, `log`), we enable automatic differentiation through the `Dual` class.

---

## Installation

To install **dual_autodiff**, simply use the following pip command:

```bash
pip install -e .
```
This command installs the package in editable mode, which is helpful for development purposes. Changes made to the code are immediately reflected without the need for reinstallation.

Usage

Basic Example with the Dual Class
The Dual class represents a dual number with real and dual parts, enabling automatic differentiation.
```python
from dual_autodiff import Dual

# Initialise a dual number with real part 2.0 and dual part 1.0
x = Dual(2.0, 1.0)

# Perform operations on the dual number
y = x ** 2  # Computes x^2 using the Dual class
print(y)  # Expected output: Dual(real=4.0, dual=4.0)
```
The result’s real part is the value of the function, and the dual part provides the derivative.

Using the differentiate Function
The differentiate function allows you to compute the derivative of a function at a specific point.
```python
from dual_autodiff.autodiff_tools import differentiate

# Define a function for differentiation
def func(x):
    return x ** 2 + 3 * x

# Compute the derivative at x=3
derivative_at_3 = differentiate(func, 3.0)
print(derivative_at_3)  # Expected output: derivative value at x=3
```
This function initialises a dual number with a dual component of 1 to propagate derivative information through the computation.

API Documentation

The Dual Class
The Dual class provides support for arithmetic operations and elementary functions on dual numbers, allowing automatic differentiation. Key methods include:

__add__: Adds two dual numbers or a dual number and a float.
__sub__: Subtracts a dual number or a float.
__mul__: Multiplies by another dual number or a float.
__truediv__: Divides by another dual number or a float.
sin(): Computes the sine of a dual number.
cos(): Computes the cosine of a dual number.
exp(): Computes the exponential function.
log(): Computes the natural logarithm, raising a ValueError for non-positive inputs.
differentiate Function
The differentiate function calculates the derivative of a function at a specified point. It operates by initialising a dual number with a dual component of 1, allowing derivatives to propagate through the function.

Analytical Solutions and Test Cases

This package includes several test cases with expected analytical solutions to verify correctness:

Quadratic Function $f(x) = x^2$: Expected derivative at $x = 3$ is 6.
Trigonometric Function $f(x) = \sin(x)$: Expected derivative at $x = 0$ is 1.
Composite Function $f(x) = e^x \cdot \ln(x)$: Expected derivative at $x = 2$ is $e^2 \cdot (\ln(2) + 0.5)$.
Refer to the analytical solutions section for further details.

Summary of Expected Values
--------------------------

.. list-table:: Expected Derivative Values
   :header-rows: 1

   * - Function
     - Test Input
     - Expected Derivative
   * - Quadratic Function $f(x) = x^2$
     - $x = 3$
     - 6
   * - Trigonometric Function $f(x) = \sin(x)$
     - $x = 0$
     - 1
   * - Composite Function $f(x) = e^x \cdot \ln(x)$
     - $x = 2$
     - $e^2 \cdot (\ln(2) + 0.5)$



