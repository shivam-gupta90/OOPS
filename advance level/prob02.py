# - Magic Methods Practice
# - Create a class `ComplexNumber`
# - Implement `__add__`, `__sub__`, `__str__`

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real    # Real part
        self.imag = imag    # Imaginary part

    def __add__(self, other):
        """Add two complex numbers."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        """Subtract two complex numbers."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __str__(self):
        """Return a human-readable complex number."""
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

print("c1 =", c1)               # 3 + 4i
print("c2 =", c2)               # 1 - 2i

result_add = c1 + c2
result_sub = c1 - c2

print("Addition:", result_add)     # 4 + 2i
print("Subtraction:", result_sub) # 2 + 6i
