cdef class Dual:
    cdef public double real
    cdef public double dual
    
    # Special methods need to be declared as 'cdef inline'
    cdef inline Dual _add(self, Dual other)
    cdef inline Dual _sub(self, Dual other)
    cdef inline Dual _mul(self, Dual other)
    cdef inline Dual _truediv(self, Dual other)