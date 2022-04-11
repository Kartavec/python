"""Первый способ:"""


def my_func(x, y):
    while x > 0 and y < 0:
        return x ** y
    else:
        print('Аргументы не соответствуют условию.')


first_arg = int(input('Введите действительное положительное число: '))
second_arg = int(input('Введите целое отрицательное число: '))
print(my_func(first_arg, second_arg))

"""Второй способ:"""


def my_func_2(a, b):
    while a > 0 and b < 0:
        return pow(a, b)
    else:
        print('Аргументы не соответствуют условию.')


print(
    my_func_2(
        a=int(input('Введите действительное положительное число: ')),
        b=int(input('Введите целое отрицательное число: '))
    )
)


"""Третий спопсоб:"""


def my_func_3(c, d):
    while first > 0 and second < 0:
        i = 3
        q = c * c
        while i <= abs(d):
            i += 1
            q *= c
        return 1 / q
    else:
        print('Аргументы не соответствуют условию.')


first = int(input('Введите действительное положительное число: '))
second = int(input('Введите целое отрицательное число: '))
print(my_func_3(first, second))
