## The Dual Class

The `Dual` class supports arithmetic operations and elementary functions on dual numbers for forward-mode automatic differentiation. It enables calculations involving both function values and their derivatives. Key attributes and methods include:

- **Attributes:**
  - `real`: The real part of the dual number, representing the function value.
  - `dual`: The dual part of the dual number, representing the derivative.

- **Initialisation:**
  - `__init__(real: float, dual: float = 0)`: Initialises a `Dual` number with specified real and dual components. The default dual part is `0`.

- **Special Methods for Arithmetic Operations:**
  - `__add__(other: Union[Dual, float]) -> Dual`: Adds a dual number or a float to the current `Dual` instance. Returns a new `Dual` instance with the sum of both real and dual parts.
  - `__sub__(other: Union[Dual, float]) -> Dual`: Subtracts a dual number or a float from the current `Dual` instance.
  - `__mul__(other: Union[Dual, float]) -> Dual`: Multiplies the current `Dual` instance by another dual number or a float, applying the product rule for derivatives.
  - `__truediv__(other: Union[Dual, float]) -> Dual`: Divides the current `Dual` instance by another dual number or a float, applying the quotient rule.

- **Elementary Functions:**
  - `sin() -> Dual`: Computes the sine of a dual number. The real part is the sine of the real component, and the dual part is the derivative calculated as `dual * cos(real)`.
  - `cos() -> Dual`: Computes the cosine of a dual number. The real part is the cosine of the real component, and the dual part is calculated as `-dual * sin(real)`.
  - `exp() -> Dual`: Computes the exponential function. The real part is the exponential of the real component, and the dual part is `dual * exp(real)`.
  - `log() -> Dual`: Computes the natural logarithm, with the real part as `log(real)`. Raises a `ValueError` if the real component is non-positive (as logarithm is undefined for non-positive values).

## The Cython Implementation of the Dual Class

To improve performance, a Cython version of the `Dual` class is available in `dual_autodiffx`. Key optimisations include:

- **Typed Attributes:**
  - `cdef public double real`
  - `cdef public double dual`

- **Inline Arithmetic Methods:**
  - Methods like `_add`, `_sub`, `_mul`, and `_truediv` are implemented inline in Cython to reduce overhead and improve performance for arithmetic operations.

## differentiate Function

The `differentiate` function calculates the derivative of a function at a specified point by initializing a dual number with a dual component of 1, allowing derivatives to propagate through the function. It works by calling the function with the dual number and returning the dual part of the result, which represents the derivative.

- **Arguments:**
  - `f (Callable[[Dual], Dual])`: The function to differentiate, which should accept a single argument of type `Dual` and return a `Dual` instance.
  - `x (float)`: The point at which to evaluate the derivative.

- **Returns:**
  - `float`: The derivative of `f` at `x`, as captured by the dual part of the output.
