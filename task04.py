from task01 import convert_to_int


def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def check_for_positive(value):
    try:
        if value <= 0:
            return None
    except TypeError:
        return None
    return value


def check_for_negative(value):
    try:
        if value >= 0:
            return None
    except TypeError:
        return None
    return value


def exponentiation_easy_way(base, power):
    return base ** power


def exponentiation_hard_way(base, power):
    divider = base
    for i in range(abs(power)-1):
        divider = divider * base

    result = 1 / divider

    return result


def main():
    base = convert_to_float(input('Введите действительное положительное число: '))

    if base is None or check_for_positive(base) is None:
        print('Необходимо ввести действительное положительное число!')
        return

    power = convert_to_int(input('Введите целое отрицательное число: '))

    if power is None or check_for_negative(power) is None:
        print('Необходимо ввести целое отрицательное число!')
        return

    result_easy_way = exponentiation_easy_way(base, power)
    result_hard_way = exponentiation_hard_way(base, power)

    print(f'Результат вычисления простым путём: {result_easy_way}')
    print(f'Результат вычисления сложным путём: {result_hard_way}')


if __name__ == '__main__':
    main()
