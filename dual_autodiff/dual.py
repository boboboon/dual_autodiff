"""Handles our dual class."""

import math
from typing import Union


class Dual:
    """A class to represent a dual number, which enables forward-mode automatic differentiation.

    Attributes:
        real (float): The real part of the dual number.
        dual (float): The dual part of the dual number, representing the derivative.
    """

    def __init__(self, real: float, dual: float = 0) -> None:
        """Initializes a Dual number with a real and dual component.

        Args:
            real (float): The real part of the dual number.
            dual (float, optional): The dual part of the dual number, representing the derivative,
            defaults to 0.
        """
        self.real = real
        self.dual = dual

    def __repr__(self) -> str:
        """Returns a string representation of the Dual number."""
        return f"Dual(real={self.real}, dual={self.dual})"

    def __add__(self, other: Union["Dual", float]) -> "Dual":
        """Adds a Dual number or a float to the current Dual number."""
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        return Dual(self.real + other, self.dual)

    def __sub__(self, other: Union["Dual", float]) -> "Dual":
        """Subtracts a Dual number or a float from the current Dual number."""
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        return Dual(self.real - other, self.dual)

    def __mul__(self, other: Union["Dual", float]) -> "Dual":
        """Multiplies the current Dual number by another Dual number or a float."""
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        return Dual(self.real * other, self.dual * other)

    def __truediv__(self, other: Union["Dual", float]) -> "Dual":
        """Divides the current Dual number by another Dual number or a float."""
        if isinstance(other, Dual):
            real = self.real / other.real
            dual = (self.dual * other.real - self.real * other.dual) / (other.real**2)
            return Dual(real, dual)
        return Dual(self.real / other, self.dual / other)

    def sin(self) -> "Dual":
        """Returns the sine of the Dual number.

        Returns:
            Dual: The result of applying the sine function.
        """
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))

    def cos(self) -> "Dual":
        """Returns the cosine of the Dual number.

        Returns:
            Dual: The result of applying the cosine function.
        """
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))

    def exp(self) -> "Dual":
        """Returns the exponential of the Dual number.

        Returns:
            Dual: The result of applying the exponential function.
        """
        exp_real = math.exp(self.real)
        return Dual(exp_real, self.dual * exp_real)

    def log(self) -> "Dual":
        """Returns the natural logarithm of the Dual number.

        Raises:
            ValueError: If the real part is non-positive (logarithm undefined).

        Returns:
            Dual: The result of applying the natural logarithm function.
        """
        if self.real > 0:
            return Dual(math.log(self.real), self.dual / self.real)
        negative_log_err = "Logarithm of non-positive value is undefined for Dual numbers."
        raise ValueError(negative_log_err)
