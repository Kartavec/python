from task01 import convert_to_int


def sum_of_the_biggest_args(a, b, c):
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    term1, term2 = numbers[:2]

    return term1 + term2


def main():
    a = convert_to_int(input('Введите первое число: '))
    if a is None:
        print('Некорректный ввод, необходимо ввести число!')
        return

    b = convert_to_int(input('Введите второе число: '))
    if b is None:
        print('Некорректный ввод, необходимо ввести число!')
        return

    c = convert_to_int(input('Введите третье число: '))
    if c is None:
        print('Некорректный ввод, необходимо ввести число!')
        return

    result = sum_of_the_biggest_args(a, b, c)
    print(f'Сумма двух наибольших чисел равна {result}.')


if __name__ == '__main__':
    main()
