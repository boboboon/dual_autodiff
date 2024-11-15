"""Handles the differentiation of functions using the Dual class for automatic differentiation."""

from typing import Callable

from .dual import Dual


def differentiate(f: Callable[[Dual], Dual], x: float) -> float:
    """Computes the derivative of a function `f` at a given point `x` using dual numbers.

    This function leverages forward-mode automatic differentiation by initializing
    a dual number with a dual component of 1, which captures the derivative information
    in the dual part of the result after applying `f`.

    Args:
        f (Callable[[Dual], Dual]): The function to differentiate, which should accept a
            single argument of type Dual and return a Dual instance.
        x (float): The point at which to evaluate the derivative.

    Returns:
        float: The derivative of `f` at `x`, as captured by the dual part of the output.
    """
    x_dual = Dual(x, 1)  # Dual number with real=x and dual=1 for derivative computation
    result = f(x_dual)
    return result.dual  # The dual component represents the derivative
