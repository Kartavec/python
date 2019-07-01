# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def sliyanie(mas, start, end):

    if end - start == 1:

        if mas[start] > mas[end]:
            mas[start], mas[end] = mas[end], mas[start]

        return

    elif end == start:

        return

    des = start + (end - start) // 2
    sliyanie(mas, start, des)
    sliyanie(mas, des + 1, end)

    left_idx = start
    right_idx = des + 1

    result = []
    while left_idx <= des or right_idx <= end:

        if right_idx > end or (left_idx <= des and mas[left_idx] < mas[right_idx]):
            result.append(mas[left_idx])
            left_idx += 1
        elif left_idx > des or (right_idx <=end and mas[left_idx] > mas[right_idx]):
            result.append(mas[right_idx])
            right_idx += 1

    i = 0
    while start + i <= end:
        mas[start + i] = result[i]
        i += 1

MAX = 50
MIN = 0

mas = [i for i in range(MIN, MAX)]

random.shuffle(mas)
print("исходный массив", mas)

sliyanie(mas, 0, MAX - MIN - 1)

print("отсортированный массив", mas)