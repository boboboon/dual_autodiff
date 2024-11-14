The **dual_autodiff** library leverages dual numbers for forward-mode automatic differentiation, useful in fields like optimization, machine learning, and scientific computing.

## Dual Numbers and Automatic Differentiation

Dual numbers extend real numbers to compute derivatives via symbolic propagation. A dual number is expressed as:

$$
x = a + b \epsilon
$$

where:

- **a** is the real part,
- **b** is the dual part (the derivative), and
- **ε** is an infinitesimal element with the property: \( \epsilon^2 = 0 \).

By defining operations like addition, multiplication, and elementary functions (e.g., `sin`, `cos`, `exp`, `log`), we enable automatic differentiation through the `Dual` class.
