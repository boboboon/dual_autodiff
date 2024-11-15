The `Dual` class in `dual_autodiff` represents a dual number, which has two components: a real part and a dual part. This class allows for automatic differentiation by tracking the function's value through the real component and the derivative through the dual component.

## Python Usage Example

```python
from dual_autodiff import Dual

# Initialise a dual number with real part 2.0 and dual part 1.0
x = Dual(2.0, 1.0)

# Perform operations on the dual number
y = x ** 2  # Computes x^2 using the Dual class
print(y)  # Expected output: Dual(real=4.0, dual=4.0)
```

In this example:

- The real part represents the actual function value at a given point.
- The dual part represents the derivative at that point.

After creating `x = Dual(2.0, 1.0)`, squaring `x` to get `y = x ** 2` results in `y` having:

- A real component of $2.0^2 = 4.0$
- A dual component calculated as $2.0 \times 2 \times 1.0 = 4.0$

Thus, `y` represents both the value $f(x) = x^2$ and the derivative $f'(x) = 2x$ at $x=2$.

## Using the differentiate Function

The `differentiate` function automates this process by calculating the derivative of a given function at a specific point:

```python
from dual_autodiff.autodiff import differentiate

# Define a function for differentiation
def func(x):
    return x ** 2 + 3 * x

# Compute the derivative at x=3
derivative_at_3 = differentiate(func, 3.0)
print(derivative_at_3)  # Expected output: derivative value at x=3
```

Here, `differentiate` creates a dual number at $x=3$ with a dual component of 1 (to propagate derivative information). It calculates the function’s value and derivative at that point, then returns the derivative part.

## Cython Implementation

To optimise performance, `dual_autodiff` also provides a Cython-implemented version of the `Dual` class in `dual_autodiffx`. The Cython version uses `cdef` to define class members and methods, allowing for faster execution.

### Key Cython Code Structure for the Dual Class

```cython
cdef class Dual:
    cdef public double real
    cdef public double dual

    def __init__(self, double real, double dual=0.0):
        self.real = real
        self.dual = dual
```

In this Cython class:

- `cdef` allows for specifying types like `double`, which improves performance by avoiding Python's dynamic typing.
- `public` enables access to `real` and `dual` from outside the class, similar to a public attribute in Python.

### Cython Methods for Arithmetic Operations

Cython's `cdef inline` methods define the core operations $(+, -, \times, \div)$ for dual numbers. These methods are optimised with low-level C-like operations for speed.

#### Addition

```cython
cdef inline Dual _add(self, Dual other):
    return Dual(self.real + other.real, self.dual + other.dual)
```

The `_add` method adds the real parts and dual parts of two `Dual` instances.

#### Multiplication

```cython
cdef inline Dual _mul(self, Dual other):
    return Dual(
        self.real * other.real,
        self.real * other.dual + self.dual * other.real
    )
```

The `_mul` method implements dual number multiplication:

- The real component is the product of the two real parts.
- The dual component is calculated by applying the product rule, yielding `self.real * other.dual + self.dual * other.real`.

#### Division

```cython
cdef inline Dual _truediv(self, Dual other):
    cdef double denom = other.real * other.real
    return Dual(
        self.real / other.real,
        (self.dual * other.real - self.real * other.dual) / denom
    )
```

For division:

- The real component is the quotient of the real parts.
- The dual component is computed using the quotient rule.

### Cython Differentiate Function

The `differentiate` function in Cython calculates derivatives by creating a dual number and propagating it through a function:

```cython
from dual_autodiffx.dual cimport Dual

cpdef double differentiate(f, double x):
    """Computes the derivative of a function `f` at a given point `x` using dual numbers."""
    cdef Dual x_dual = Dual(x, 1.0)
    cdef Dual result = f(x_dual)
    return result.dual
```

- `cpdef` allows the function to be called from both C and Python, improving flexibility.
- A dual number `x_dual = Dual(x, 1.0)` is initialised with the real part as `x` and the dual part as `1.0`.
- The function `f` is called with `x_dual`, propagating the dual part through the computation.
- Finally, the function returns `result.dual`, representing the derivative of `f` at `x`.

This Cython implementation is significantly faster than its Python counterpart because of the `cdef` optimisations and direct C-level operations on floating-point numbers.
