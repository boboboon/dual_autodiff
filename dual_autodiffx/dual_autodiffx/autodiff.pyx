from dual_autodiffx.dual cimport Dual

cpdef double differentiate(f, double x):
    """Computes the derivative of a function `f` at a given point `x` using dual numbers."""
    cdef Dual x_dual = Dual(x, 1.0)
    cdef Dual result = f(x_dual)
    return result.dual
