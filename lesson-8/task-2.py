from helper import int_input


class MyZeroDivisionExtension(Exception):
    pass


class Number:
    def __init__(self, num: int):
        self.num = num

    def __truediv__(self, other):
        if other.num == 0:
            raise MyZeroDivisionExtension('Division by zero')
        return self.num/other.num


number1 = Number(int_input('Enter number 1: '))
number2 = Number(int_input('Enter number 2: '))

try:
    print('Div: ', number1 / number2)
except MyZeroDivisionExtension as e:
    print(e.__class__.__name__, ':', e)
