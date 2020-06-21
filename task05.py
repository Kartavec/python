def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return False


def parse_complex_number(number):
    number = number.replace(' ', '')

    first_sign = '+'
    if number[0] == '+':
        number = number[1:]
    if number[0] == '-':
        number = number[1:]
        first_sign = '-'

    try:
        real_part, imaginary_part = number.split('+')
        second_sign = '+'
    except ValueError:
        try:
            real_part, imaginary_part = number.split('-')
            second_sign = '-'
        except ValueError:
            return False

    if imaginary_part[-1] != 'i':
        return False

    if imaginary_part == 'i':
        imaginary_part = 1
    else:
        imaginary_part = imaginary_part[:-1]

    real_part = convert_to_int(real_part)
    imaginary_part = convert_to_int(imaginary_part)

    if real_part and imaginary_part:
        if first_sign == '-':
            real_part = -real_part
        if second_sign == '-':
            imaginary_part = -imaginary_part
        return real_part, imaginary_part

    return False


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        try:
            assert isinstance(real_part, int)
            assert isinstance(imaginary_part, int)
        except AssertionError:
            print('Wrong input arguments! Instance was not create!')
            return
        self.r_part = real_part
        self.i_part = imaginary_part

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return
        new_r_part = self.r_part + other.r_part
        new_i_part = self.i_part + other.i_part
        return ComplexNumber(new_r_part, new_i_part)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            return

        a1 = self.r_part
        a2 = other.r_part
        b1 = self.i_part
        b2 = other.i_part

        new_r_part = a1 * a2 - b1 * b2
        new_i_part = a1 * b2 + b1 * a2

        return ComplexNumber(new_r_part, new_i_part)

    def __str__(self):
        if self.i_part > 0:
            sign = '+'
            i_part = self.i_part
        elif self.i_part == 0:
            sign = '+'
            i_part = ''
        else:
            i_part = abs(self.i_part)
            sign = '-'

        if abs(i_part) == 1:
            i_part = ''

        return f'{self.r_part} {sign} {i_part}i'


def get_input(message):
    while True:
        first_input = input(message)
        parsed_input = parse_complex_number(first_input)
        if parsed_input:
            return parsed_input
        print('Некорректный ввод, попробуйте еще раз...')


if __name__ == '__main__':
    first_r_part, first_i_part = get_input('Введите первое комплексное число в формате "45 + 39i"')
    second_r_part, second_i_part = get_input('Введите второе комплексное число в формате "45 + 39i"')
    first_complex_number = ComplexNumber(first_r_part, first_i_part)
    second_complex_number = ComplexNumber(second_r_part, second_i_part)

    print('Результат сложения двух комплексных чисел:')
    print(first_complex_number + second_complex_number)
    print()

    print('Результат умножения двух комплексных числе:')
    print(first_complex_number * second_complex_number)
    print()
