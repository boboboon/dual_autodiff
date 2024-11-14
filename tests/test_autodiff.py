"""Our test folder for differentiation."""

import math

from dual_autodiff.autodiff import differentiate
from dual_autodiff.dual import Dual


def test_differentiate_basic_function() -> None:
    """Test differentiation of a basic quadratic function."""

    def f(x: Dual) -> Dual:
        return x * x  # f(x) = x^2, derivative at x should be 2*x

    derivative_at_3 = differentiate(f, 3)
    diff_basic_err = "Differentiation failed for f(x) = x^2: Expected derivative at x=3 to be 6"
    if derivative_at_3 != 6:
        raise ValueError(diff_basic_err)


def test_differentiate_trig_function() -> None:
    """Test differentiation of a trigonometric sine function."""

    def f(x: Dual) -> Dual:
        return x.sin()  # derivative of sin(x) is cos(x)

    derivative_at_0 = differentiate(f, 0)
    diff_trig_err = "Differentiation failed for f(x) = sin(x): Expected derivative at x=0 to be 1"
    if not math.isclose(derivative_at_0, 1.0, rel_tol=1e-5):
        raise ValueError(diff_trig_err)


def test_differentiate_exp_log_function() -> None:
    """Test differentiation of a composite exponential and logarithmic function."""

    def f(x: Dual) -> Dual:
        return x.exp() * x.log()  # f(x) = exp(x) * log(x)

    derivative_at_2 = differentiate(f, 2)
    expected = math.exp(2) * (1 + math.log(2))  # Analytical derivative
    diff_exp_log_err = (
        "Differentiation failed for f(x) = exp(x) * log(x): "
        "Expected derivative at x=2 to be close to the analytical solution"
    )
    if not math.isclose(derivative_at_2, expected, rel_tol=1e-5):
        raise ValueError(diff_exp_log_err)
