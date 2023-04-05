"""
Задание 4.
Пользователь вводит целое положительное
число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и
арифметические операции.
"""


num = int(input('Введите целое число: '))
maxx = 0
list_of_num = [int(i) for i in str(num)]

while list_of_num:
    n = list_of_num.pop()
    maxx = n if n > maxx else maxx
    if maxx == 9:
        break
print(f'Максимальная цифра: {maxx}')
