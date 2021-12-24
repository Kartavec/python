"""
1.Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
2.a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
операции!
2.b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.
3.* Решить задачу под пунктом b, не создавая новый список.
"""

base_list = list()

for i in range(1, 1000):
    if i % 2 != 0:
        i = i**3
        base_list.append(i)
    else:
        continue

# 2.a)

digit_sum = 0  # Сумма цифр в числе
summ = 0  # Сумма чисел

for number in base_list:
    tmp = number
    while tmp != 0:
        digit_sum += tmp % 10
        tmp = tmp // 10

    if digit_sum % 7 == 0:
        digit_sum = 0
        summ += number
    else:
        digit_sum = 0

print(summ)

# 2.b)/3

summ_add_seventeen = 0 # Сумма чисел

for number in base_list:
    number += 17
    tmp = number

    while tmp != 0:
        digit_sum += tmp % 10
        tmp //= 10

    if digit_sum % 7 == 0:
        digit_sum = 0
        summ_add_seventeen += number
        print(number)
    else:
        digit_sum = 0

print(summ_add_seventeen)
