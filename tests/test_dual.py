"""Our test script for our dual class."""

import math

import pytest

from dual_autodiff.dual import Dual


def test_initialization() -> None:
    """Test initialization of Dual with real and dual parts."""
    x = Dual(2, 1)
    init_real_err = "Initialization failed: Expected real part to be 2"
    if not x.real == 2:
        raise ValueError(init_real_err)

    init_dual_err = "Initialization failed: Expected dual part to be 1"
    if not x.dual == 1:
        raise ValueError(init_dual_err)


def test_addition() -> None:
    """Test addition operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x + y

    add_real_err = "Addition failed: Expected real part to be 5 after addition"
    if not result.real == 5:
        raise ValueError(add_real_err)

    add_dual_err = "Addition failed: Expected dual part to be 3 after addition"
    if not result.dual == 3:
        raise ValueError(add_dual_err)


def test_subtraction() -> None:
    """Test subtraction operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x - y

    sub_real_err = "Subtraction failed: Expected real part to be -1 after subtraction"
    if not result.real == -1:
        raise ValueError(sub_real_err)

    sub_dual_err = "Subtraction failed: Expected dual part to be -1 after subtraction"
    if not result.dual == -1:
        raise ValueError(sub_dual_err)


def test_multiplication() -> None:
    """Test multiplication operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x * y

    mul_real_err = "Multiplication failed: Expected real part to be 6 after multiplication"
    if not result.real == 6:
        raise ValueError(mul_real_err)

    mul_dual_err = "Multiplication failed: Expected dual part to be 7 after multiplication"
    if not result.dual == 7:
        raise ValueError(mul_dual_err)


def test_division() -> None:
    """Test division operation for Dual numbers."""
    x = Dual(4, 1)
    y = Dual(2, 1)
    result = x / y

    div_real_err = "Division failed: Expected real part to be 2 after division"
    if not result.real == 2:
        raise ValueError(div_real_err)

    div_dual_err = "Division failed: Expected dual part to be -0.5 after division"
    if not math.isclose(result.dual, -0.5, rel_tol=1e-5):
        raise ValueError(div_dual_err)


def test_sin() -> None:
    """Test sine function for Dual numbers."""
    x = Dual(math.pi / 2, 1)
    result = x.sin()

    sin_real_err = "Sine function failed: Expected real part to be close to 1.0 for sin(pi/2)"
    if not math.isclose(result.real, 1.0, rel_tol=1e-5):
        raise ValueError(sin_real_err)

    sin_dual_err = "Sine function failed: Expected dual part to be close to 0.0 for sin(pi/2)"
    if not math.isclose(result.dual, 0.0, rel_tol=1e-5):
        raise ValueError(sin_dual_err)


def test_cos() -> None:
    """Test cosine function for Dual numbers."""
    x = Dual(math.pi, 1)
    result = x.cos()

    cos_real_err = "Cosine function failed: Expected real part to be close to -1.0 for cos(pi)"
    if not math.isclose(result.real, -1.0, rel_tol=1e-5):
        raise ValueError(cos_real_err)

    cos_dual_err = "Cosine function failed: Expected dual part to be close to 0.0 for cos(pi)"
    if not math.isclose(result.dual, 0.0, rel_tol=1e-5):
        raise ValueError(cos_dual_err)


def test_exp() -> None:
    """Test exponential function for Dual numbers."""
    x = Dual(1, 1)
    result = x.exp()

    exp_real_err = "Exponential function failed: Expected real part to be close to e for exp(1)"
    if not math.isclose(result.real, math.e, rel_tol=1e-5):
        raise ValueError(exp_real_err)

    exp_dual_err = "Exponential function failed: Expected dual part to be close to e for exp(1)"
    if not math.isclose(result.dual, math.e, rel_tol=1e-5):
        raise ValueError(exp_dual_err)


def test_log() -> None:
    """Test logarithm function for Dual numbers, including exception on invalid input."""
    x = Dual(math.e, 1)
    result = x.log()

    log_real_err = "Logarithm function failed: Expected real part to be 1.0 for log(e)"
    if not math.isclose(result.real, 1.0, rel_tol=1e-5):
        raise ValueError(log_real_err)

    log_dual_err = "Logarithm function failed: Expected dual part to be 1/e for log(e)"
    if not math.isclose(result.dual, 1 / math.e, rel_tol=1e-5):
        raise ValueError(log_dual_err)

    log_error_msg = (
        "Logarithm function failed: Logarithm of non-positive value is undefined for Dual numbers."
    )
    with pytest.raises(ValueError, match=log_error_msg):
        Dual(-1, 1).log()  # Should raise an error for non-positive values
