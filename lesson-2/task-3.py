# coding=utf-8
valid = False
while not valid:
    try:
        month_num = int(input('Введите номер месяца (1-12): '))
    except ValueError:
        print('Ошибка ввода')
        continue
    if month_num < 1 or month_num > 12:
        print('Вы ввели несуществующий месяц')
        continue
    valid = True

seasons = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11],
}

for k, s in seasons.items():
    if month_num in s:
        print('Время года: %s' % (k))
        break
