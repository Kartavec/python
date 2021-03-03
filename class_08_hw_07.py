# Class 08
# Task 07
# A  script that creates ComplexNumber class


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'The sum of z1 and z2 equals to')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'The product of z1 and z2 equals to')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
