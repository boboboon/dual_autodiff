"""Our test folder for differentiation."""

import math

from dual_autodiff.autodiff import differentiate
from dual_autodiff.dual import Dual

REL_TOL = 1e-5


def test_differentiate_basic_function() -> None:
    """Test differentiation of a basic quadratic function."""

    def f(x: Dual) -> Dual:
        return x * x  # f(x) = x^2, derivative at x should be 2*x

    derivative_at_3 = differentiate(f, 3)
    # Error message for differentiation of f(x) = x^2 at x=3
    diff_basic_err = f"Differentiation failed for f(x) = x^2 at x=3, got {derivative_at_3}"
    if not math.isclose(derivative_at_3, 6, rel_tol=REL_TOL):
        raise ValueError(diff_basic_err)


def test_differentiate_trig_function() -> None:
    """Test differentiation of a trigonometric sine function."""

    def f(x: Dual) -> Dual:
        return x.sin()  # derivative of sin(x) is cos(x)

    derivative_at_0 = differentiate(f, 0)
    # Error message for differentiation of f(x) = sin(x) at x=0
    diff_trig_err = f"Differentiation failed for f(x) = sin(x) at x=0, got {derivative_at_0}"
    if not math.isclose(derivative_at_0, 1.0, rel_tol=REL_TOL):
        raise ValueError(diff_trig_err)


def test_differentiate_exp_log_function() -> None:
    """Test differentiation of a composite exponential and logarithmic function."""

    def f(x: Dual) -> Dual:
        return x.exp() * x.log()  # f(x) = exp(x) * log(x)

    derivative_at_2 = differentiate(f, 2)
    expected = math.exp(2) * (math.log(2) + 0.5)
    # Error message for differentiation of f(x) = exp(x) * log(x) at x=2
    diff_exp_log_err = (
        f"Differentiation failed for f(x) = exp(x) * log(x) at x=2, got {derivative_at_2}"
    )
    if not math.isclose(derivative_at_2, expected, rel_tol=REL_TOL):
        raise ValueError(diff_exp_log_err)
