"""
Задание 1.
Реализовать скрипт, в котором должна быть предусмотрена
функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка
в час) + премия. Во время выполнения расчёта для
конкретных значений необходимо запускать скрипт с параметрами.
"""


import sys

if len(sys.argv) > 1:
    hours, salary_per_our, bonus = map(float, sys.argv[1:])
else:
    hours = int(input('Введите кол-во отработанных часов: '))
    salary_per_our = int(input('Введите ставку: '))
    bonus = int(input('Введите премию: '))


def count_salaru(hours, salary_per_our, bonus):
    return f'Зарплата: {hours * salary_per_our + bonus}'


print(count_salaru(hours, salary_per_our, bonus))
