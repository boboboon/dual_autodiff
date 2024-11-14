# dual_autodiff
Automatic Differentiation using dual numbers

---

## Dual Numbers and Automatic Differentiation

This document explains the concepts and implementations behind dual numbers and automatic differentiation in the dual_autodiff library. It includes analytical solutions for each test case and clarifies the expected behavior of the Dual class and `differentiate` function.

---

## Table of Contents

1. [Dual Numbers](#dual-numbers)
2. [Automatic Differentiation](#automatic-differentiation)
3. [Analytical Solutions for Test Cases](#analytical-solutions-for-test-cases)
   - [Basic Quadratic Function](#basic-quadratic-function)
   - [Trigonometric Function](#trigonometric-function)
   - [Composite Exponential and Logarithmic Function](#composite-exponential-and-logarithmic-function)
4. [Summary of Expected Values](#summary-of-expected-values)

---

## Dual Numbers

Dual numbers are an extension of the real numbers and are used in this library to facilitate automatic differentiation. A dual number is represented as:

$$
x = a + b \epsilon
$$

where:

- `a` is the real part,
- `b` is the dual part, and
- `\epsilon` is an infinitesimal element with the property: $$\epsilon^2 = 0$$

This representation enables us to differentiate functions symbolically by propagating derivatives through elementary operations.

### Implementation in Dual
The `Dual` class provides methods to perform operations on dual numbers, such as addition, subtraction, multiplication, division, and basic functions (e.g., `sin`, `cos`, `exp`, `log`), enabling differentiation without explicitly computing limits.

---

## Automatic Differentiation

Automatic Differentiation (AD) allows us to compute derivatives programmatically by propagating dual numbers through a computation graph. In this library, the `differentiate` function takes a function and a point as inputs, computes the dual form of the input, and returns the derivative of the function at that point.

---

## Analytical Solutions for Test Cases

### Basic Quadratic Function
**Test**: `test_differentiate_basic_function`

For the function:

$$
f(x) = x^2
$$

The analytical derivative is:

$$
f'(x) = 2x
$$

Therefore, at $x = 3$, we expect:

$$
f'(3) = 6
$$

### Trigonometric Function
**Test**: `test_differentiate_trig_function`

For the function:

$$
f(x) = \sin(x)
$$

The analytical derivative is:

$$
f'(x) = \cos(x)
$$

At $x = 0$, we expect:

$$
f'(0) = 1
$$

### Composite Exponential and Logarithmic Function
**Test**: `test_differentiate_exp_log_function`

For the composite function:

$$
f(x) = e^x \cdot \ln(x)
$$

The analytical derivative, using the product rule, is:

$$
f'(x) = e^x \cdot \ln(x) + e^x \cdot \frac{1}{x}
$$

Thus, at $x = 2$:

$$
f'(2) = e^2 \cdot (\ln(2) + 0.5)
$$

---

## Summary of Expected Values

| Function                                  | Test Input | Expected Derivative                           |
|-------------------------------------------|------------|-----------------------------------------------|
| Quadratic Function $f(x) = x^2$          | $x = 3$    | 6                                             |
| Trigonometric Function $f(x) = \sin(x)$  | $x = 0$    | 1                                             |
| Composite Function $f(x) = e^x \ln(x)$   | $x = 2$    | $e^2 \cdot (\ln(2) + 0.5)$                   |