first_result = int(input('Укажите дистанцию пройденную в первый день: '))
required_result = int(input(('Укажите желаемую дистанцию: ')))
print(f'Вы начинаете с {first_result}км.')
days = 0
while first_result <= required_result:
    progress = first_result + 0.1 * first_result
    print(f'Прогресс {round(progress, 2)} км.')
    first_result = progress
    days += 1
if (days % 10) <= 4 and (days % 10 > 1):
    if days >= 10 and days <= 20:
        print(f'Вы пробежите целевую дистанцию через {days} дней.')
    else:
        print(f'Вы пробежите целевую дистанцию через {days} дня.')
elif (days % 10) != 1:
    print(f'Вы пробежите целевую дистанцию через {days} дней.')
else:
    print(f'Вы пробежите целевую дистанцию через {days} день.')
