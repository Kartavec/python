class Complex_number():
    def __init__(self, number):
        self.number = str(number)
        self.number = self.number.split(' ')

    def __add__(self, other):
        a = complex(int(self.number[0]), int(self.number[2]))
        b = complex((int(other.number[0])), int(other.number[2]))
        return a + b

    def __mul__(self, other):
        a = complex(int(self.number[0]), int(self.number[2]))
        b = complex((int(other.number[0])), int(other.number[2]))
        return a * b


num1 = Complex_number('5 + 6 i')
num2 = Complex_number('10 + 16 i')
n = num1 + num2
m = num1 * num2
print(n)
print(m)
