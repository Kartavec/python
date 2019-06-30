# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import sys

MAX = 1000
mas = [random.randint(0, MAX) for i in range(MAX)]

def memoryof(value):

    rez = 0

    if type(value) is dict:
        rez += sys.getsizeof(value)
        for k, v in value.items():
            rez += memoryof(k)
            rez += memoryof(v)
    elif type(value) is list:
        rez += sys.getsizeof(value)
        for i in value:
            rez += memoryof(i)
    elif (type(value) is str) or (type(value) is int) or (type(value) is float) or (type(value) is bool):
        rez += sys.getsizeof(value)
    else:
        print(type(value), "неведомый тип, выяснить")

    return rez


def variant1(mas, val):

    dict = [{"ind": i, "val": lval} for i, lval in enumerate(mas)]

    val[0] += memoryof(dict)

    need_do = True
    val[0] += memoryof(need_do)

    while need_do:
        need_do = False
        for i in range(len(dict) - 1):
            if dict[i]["val"] > dict[i+1]["val"]:
                dict[i], dict[i+1] = dict[i+1], dict[i]
                need_do = True
        val[0] += memoryof(i)

    return [dict[0]["val"], dict[1]["val"]]

def variant2(mas, val):

    a = mas[0]
    b = mas[1]

    val[0] += memoryof(a)
    val[0] += memoryof(b)

    if a > b:
        a, b = b, a

    for i in mas:

        if i < a:
            a, b = i, a
        elif i < b:
            b = i

    val[0] += memoryof(i)

    return [a, b]

def variant3(mas, val):
    # берем половину массива, ищем в нем 2 наименьших числа
    # затем сравниваем эти 2 числа с двумя наименьшими из правой половины
    # и так рекурсивно, пока не дойдем до минимума элементов

    len_ = len(mas)
    val[0] += memoryof(len_)

    # Память этого блока учтена уже в массивах left и right
    if len_ <= 3:
        a = mas[0]
        b = mas[1]

        if a > b:
            a, b = b, a

        if len_ == 3:
            c = mas[2]
            if c < a:
                a, b = c, a
            elif c < b:
                b = c

        return [a, b]

    half = len_ // 2

    val[0] += memoryof(half)

    left = mas[:half]
    right = mas[half:]

    val[0] += memoryof(left)
    val[0] += memoryof(right)

    left = variant3(left, val)
    right = variant3(right, val)

    # Память на переменные a и b учтена в предыдущем прибавлении. Здесь только память на list
    val[0] += sys.getsizeof(left)
    val[0] += sys.getsizeof(right)

    if left[1] < right[0]:
        return left
    elif right[1] < left[0]:
        return right

    if left[0] < right[0]:
        a = left[0]
        b = right[0]
    else:
        a = right[0]
        b = left[0]

    return [a, b]

val = memoryof(mas)

print("Занято общей переменной", val, "байт")

print("*" * 5, 1, "*" * 5)

val = [0]
rez = variant1(mas, val)
print("Результат функции", rez)
print("Программа без общей переменной заняла", val[0], "байт")

print("*" * 5, 2, "*" * 5)

val = [0]
rez = variant2(mas, val)
print("Результат функции", rez)
print("Программа без общей переменной заняла", val[0], "байт")

print("*" * 5, 3, "*" * 5)

val = [0]
rez = variant3(mas, val)
print("Результат функции", rez)
print("Программа без общей переменной заняла", val[0], "байт")

# Система: core i7, 16 gb ram, x64
# РЕЗУЛЬТАТЫ:
# Занято общей переменной 18514 байт
# ***** 1 *****
# Результат функции [0, 4]
# Программа без общей переменной заняла 237868 байт
# ***** 2 *****
# Результат функции [0, 4]
# Программа без общей переменной заняла 42 байт
# ***** 3 *****
# Результат функции [0, 4]
# Программа без общей переменной заняла 259074 байт

# ВЫВОДЫ:
# Вариант 1 много кушает памяти из за неправильного применения словаря
# Вариант 2 самый правильный, т.к задача решена просто алгоритмом
# Вариант 3. Рекурсия - зло.
