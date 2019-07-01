# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def testleft(mas):
    over = 0
    less = 0
    lequal = 0
    requal = 0

    des = len(mas) // 2

    for i in range(des):
        if mas[des + i + 1] > mas[des]:
            over += 1
        elif mas[des + i + 1] == mas[des]:
            requal += 1

        if mas[i] < mas[des]:
            less += 1
        elif mas[i] == mas[des]:
            lequal += 1

    if less + lequal == over + requal:
        return 0
    elif less > over:
        return -1
    else:
        return 1


def mediana(mas):

    count = 0

    leftstart = 0
    leftend = len(mas) // 2

    rightstart = leftend + 1
    rightend = len(mas)

    testresult = testleft(mas)
    while not testresult == 0:

        result = None
        current_pos = random.randint(0, 1)

        while result == None:

            if current_pos == 1:
                eggs = range(rightstart, rightend)
            else:
                eggs = range(leftstart, leftend)

            for i in eggs:
                if mas[i] > mas[leftend] and (result is None or mas[i] < mas[result]) and testresult == 1:
                    result = i
                elif mas[i] < mas[leftend] and (result is None or mas[i] > mas[result]) and testresult == -1:
                    result = i

            current_pos = 0 if current_pos == 1 else 0

        mas[result], mas[leftend] = mas[leftend], mas[result]

        testresult = testleft(mas)

        count += 1

    return count

m = int(input("Введите m (натуральное больше 0): "))

MAX = 2*m + 1
MIN = 0

mas = [i for i in range(MIN, MAX)]
random.shuffle(mas)

print("*" * 5, "исходный массив", "*" * 5)
print(mas)

count = mediana(mas)

print("*" * 5, "расчитан за", count, "шагов", "*" * 5)
print(mas)
print("Медиана:", mas[len(mas) // 2])

mas.sort()
print("Проверка медианы:", mas[len(mas) // 2])

# Решено без сортировок.
# МОИ ЗАМЕРЫ СЛОЖНОСТИ АЛГОРИТМА:
#
# вход - 100: 34 шага, 48 шагов, 18 шагов
# вход - 1000: 182 шага, 4 шага, 47 шагов
# вход - 10000: 2830 шагов, 4226 шагов

# но на малых алгоритмах работает не очень шустро. Например [2, 7, 9, 2, 2] - требует до 27 шагов..