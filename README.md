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


 Contributions and A.I. Utilisation



## Contributions
Contributions to this project are welcome and appreciated! If you'd like to contribute:

- Fork the Repository: Start by forking this repository to your GitHub account.
- Clone Your Fork: Clone your forked repository locally to make changes.
- Develop Your Changes: Add new features, fix bugs, or improve documentation within your branch.
- Write Documentation: Clearly document any new functions, classes, or modifications to existing code.
- Submit a Pull Request (PR): Once your changes are ready, push them to your forked repository and create a pull request. In your PR description, please explain the changes you made and why they improve the project.
- All contributors are encouraged to write clean, modular, and well-documented code. Please include examples where applicable to demonstrate the intended use of new classes or functions.

## A.I. Utilisation in Development
This project has been developed with assistance from ChatGPT, an advanced AI language model. I initially draft the structure of classes, write examples, and document the main functions, and then use ChatGPT for:

- Generating Additional Examples: After writing an initial example, ChatGPT helps create additional examples to illustrate edge cases, alternate uses, or complex scenarios.
- Enhanced Documentation: ChatGPT assists in refining documentation by adding clarifications, expanding on function descriptions, and ensuring consistent terminology throughout.
- Code Review Suggestions: ChatGPT provides suggestions on code efficiency, readability, and possible edge cases, helping maintain a high standard of code quality.
- The collaboration with ChatGPT accelerates development by streamlining repetitive tasks and providing insights for a more polished and user-friendly outcome. Together, we aim to make this project accessible, efficient, and valuable for all users.