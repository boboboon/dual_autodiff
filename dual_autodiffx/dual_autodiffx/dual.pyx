cdef class Dual:
    def __init__(self, double real, double dual=0.0):
        self.real = real
        self.dual = dual
    
    cdef inline Dual _add(self, Dual other):
        return Dual(self.real + other.real, self.dual + other.dual)
    
    def __add__(self, other):
        if isinstance(other, Dual):
            return self._add(other)
        return self._add(Dual(other))
    
    cdef inline Dual _sub(self, Dual other):
        return Dual(self.real - other.real, self.dual - other.dual)
    
    def __sub__(self, other):
        if isinstance(other, Dual):
            return self._sub(other)
        return self._sub(Dual(other))
    
    cdef inline Dual _mul(self, Dual other):
        return Dual(
            self.real * other.real,
            self.real * other.dual + self.dual * other.real
        )
    
    def __mul__(self, other):
        if isinstance(other, Dual):
            return self._mul(other)
        return self._mul(Dual(other))
    
    cdef inline Dual _truediv(self, Dual other):
        cdef double denom = other.real * other.real
        return Dual(
            self.real / other.real,
            (self.dual * other.real - self.real * other.dual) / denom
        )
    
    def __truediv__(self, other):
        if isinstance(other, Dual):
            return self._truediv(other)
        return self._truediv(Dual(other))