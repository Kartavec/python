# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import timeit
import cProfile

MAX = 1000
mas = [random.randint(0, MAX) for i in range(MAX)]

def variant1(mas):

    dict = [{"ind": i, "val": val} for i, val in enumerate(mas)]

    need_do = True
    while need_do:
        need_do = False
        for i in range(len(dict) - 1):
            if dict[i]["val"] > dict[i+1]["val"]:
                dict[i], dict[i+1] = dict[i+1], dict[i]
                need_do = True

    return [dict[0]["val"], dict[1]["val"]]

def variant2(mas):

    a = mas[0]
    b = mas[1]

    if a > b:
        a, b = b, a

    for i in mas:

        if i < a:
            a, b = i, a
        elif i < b:
            b = i

    return [a, b]

def variant3(mas):
    # берем половину массива, ищем в нем 2 наименьших числа
    # затем сравниваем эти 2 числа с двумя наименьшими из правой половины
    # и так рекурсивно, пока не дойдем до минимума элементов

    len_ = len(mas)

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

    left = mas[:half]
    right = mas[half:]

    left = variant3(left)
    right = variant3(right)

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

rez = variant1(mas)
print(rez)

NUMBER = 3

cProfile.run("variant1(mas)")

print("Время вариант 1:", timeit.timeit("variant1(mas)", number=NUMBER, globals=globals()) / NUMBER)

#размер массива 1000:  931 function calls in 0.203 seconds
#размер массива 2000:  1991 function calls in 0.880 seconds
#размер массива 5000:  4952 function calls in 5.781 seconds
#размер массива 10000:  9987 function calls in 23.759 seconds
#размер массива 30000:  29642 function calls in 230.106 seconds

rez = variant2(mas)
print(rez)

cProfile.run("variant2(mas)")

print("Время вариант 2:", timeit.timeit("variant2(mas)", number=NUMBER, globals=globals()) / NUMBER)

#размер массива 1000:  4 function calls in 0.000 seconds
#размер массива 2000:  4 function calls in 0.000 seconds
#размер массива 5000:  4 function calls in 0.000 seconds
#размер массива 10000: 4 function calls in 0.001 seconds
#размер массива 30000: 4 function calls in 0.002 seconds

rez = variant3(mas)
print(rez)

cProfile.run("variant3(mas)")

print("Время вариант 3:", timeit.timeit("variant3(mas)", number=NUMBER, globals=globals()) / NUMBER)

#размер массива 1000: 1953 function calls (979 primitive calls) in 0.001 seconds
#размер массива 2000: 3905 function calls (1955 primitive calls) in 0.001 seconds
#размер массива 5000: 8193 function calls (4099 primitive calls) in 0.003 seconds
#размер массива 10000: 16385 function calls (8195 primitive calls) in 0.006 seconds
#размер массива 30000: 54465 function calls (27235 primitive calls) in 0.021 seconds

# ВЫВОДЫ:
# 1. сортировка пузырьком - очень долгая. время растет нелинейно. Похоже на O(n!)
# 2. второй вариант самый быстрый, т.к за один проход находит искомые значения, т.е О(1)
# 3. хоть и рекурсия - оказался на удивление неплохой вариант, время растет почти линейно от объема входящих значений