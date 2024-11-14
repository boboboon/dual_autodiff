"""Our test script for our dual class."""

import math

import pytest

from dual_autodiff.dual import Dual

# Define tolerances at the top of the file
REL_TOL = 1e-7
ABS_TOL = 1e-10


def test_initialization() -> None:
    """Test initialization of Dual with real and dual parts."""
    x = Dual(2, 1)
    init_real_err = f"Init failed: Expected real=2, got {x.real}"
    if not math.isclose(x.real, 2, rel_tol=REL_TOL):
        raise ValueError(init_real_err)

    init_dual_err = f"Init failed: Expected dual=1, got {x.dual}"
    if not math.isclose(x.dual, 1, rel_tol=REL_TOL):
        raise ValueError(init_dual_err)


def test_addition() -> None:
    """Test addition operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x + y

    add_real_err = f"Addition failed: Expected real=5, got {result.real}"
    if not math.isclose(result.real, 5, rel_tol=REL_TOL):
        raise ValueError(add_real_err)

    add_dual_err = f"Addition failed: Expected dual=3, got {result.dual}"
    if not math.isclose(result.dual, 3, rel_tol=REL_TOL):
        raise ValueError(add_dual_err)


def test_subtraction() -> None:
    """Test subtraction operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x - y

    sub_real_err = f"Subtraction failed: Expected real=-1, got {result.real}"
    if not math.isclose(result.real, -1, rel_tol=REL_TOL):
        raise ValueError(sub_real_err)

    sub_dual_err = f"Subtraction failed: Expected dual=-1, got {result.dual}"
    if not math.isclose(result.dual, -1, rel_tol=REL_TOL):
        raise ValueError(sub_dual_err)


def test_multiplication() -> None:
    """Test multiplication operation for Dual numbers."""
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x * y

    mul_real_err = f"Multiplication failed: Expected real=6, got {result.real}"
    if not math.isclose(result.real, 6, rel_tol=REL_TOL):
        raise ValueError(mul_real_err)

    mul_dual_err = f"Multiplication failed: Expected dual=7, got {result.dual}"
    if not math.isclose(result.dual, 7, rel_tol=REL_TOL):
        raise ValueError(mul_dual_err)


def test_division() -> None:
    """Test division operation for Dual numbers."""
    x = Dual(4, 1)
    y = Dual(2, 1)
    result = x / y

    div_real_err = f"Division failed: Expected real=2, got {result.real}"
    if not math.isclose(result.real, 2, rel_tol=REL_TOL):
        raise ValueError(div_real_err)

    div_dual_err = f"Division failed: Expected dual=-0.5, got {result.dual}"
    if not math.isclose(result.dual, -0.5, rel_tol=REL_TOL):
        raise ValueError(div_dual_err)


def test_sin() -> None:
    """Test sine function for Dual numbers."""
    x = Dual(math.pi / 2, 1)
    result = x.sin()

    sin_real_err = f"Sine failed: Expected real≈1.0 for sin(pi/2), got {result.real}"
    if not math.isclose(result.real, 1.0, rel_tol=REL_TOL):
        raise ValueError(sin_real_err)

    # Use ABS_TOL for the near-zero dual part
    sin_dual_err = f"Sine failed: Expected dual≈0.0 for sin(pi/2), got {result.dual}"
    if not math.isclose(result.dual, 0.0, abs_tol=ABS_TOL):
        raise ValueError(sin_dual_err)


def test_cos() -> None:
    """Test cosine function for Dual numbers."""
    x = Dual(math.pi, 1)
    result = x.cos()

    cos_real_err = f"Cosine failed: Expected real≈-1.0 for cos(pi), got {result.real}"
    if not math.isclose(result.real, -1.0, rel_tol=REL_TOL):
        raise ValueError(cos_real_err)

    # Use ABS_TOL for the near-zero dual part
    cos_dual_err = f"Cosine failed: Expected dual≈0.0 for cos(pi), got {result.dual}"
    if not math.isclose(result.dual, 0.0, abs_tol=ABS_TOL):
        raise ValueError(cos_dual_err)


def test_exp() -> None:
    """Test exponential function for Dual numbers."""
    x = Dual(1, 1)
    result = x.exp()

    exp_real_err = f"Exp failed: Expected real≈e for exp(1), got {result.real}"
    if not math.isclose(result.real, math.e, rel_tol=REL_TOL):
        raise ValueError(exp_real_err)

    exp_dual_err = f"Exp failed: Expected dual≈e for exp(1), got {result.dual}"
    if not math.isclose(result.dual, math.e, rel_tol=REL_TOL):
        raise ValueError(exp_dual_err)


def test_log() -> None:
    """Test logarithm function for Dual numbers, including exception on invalid input."""
    x = Dual(math.e, 1)
    result = x.log()

    log_real_err = f"Log failed: Expected real≈1.0 for log(e), got {result.real}"
    if not math.isclose(result.real, 1.0, rel_tol=REL_TOL):
        raise ValueError(log_real_err)

    log_dual_err = f"Log failed: Expected dual≈1/e for log(e), got {result.dual}"
    if not math.isclose(result.dual, 1 / math.e, rel_tol=REL_TOL):
        raise ValueError(log_dual_err)

    log_error_msg = "Logarithm of non-positive value is undefined for Dual numbers."
    with pytest.raises(ValueError, match=log_error_msg):
        Dual(-1, 1).log()  # Should raise an error for non-positive values
