profit = int(input('Укажите выручку за квартал: '))
cost = int(input('Укажите расходы за квартал: '))
if profit > cost:
    print(f'В прошедшем квартале наблюдается прибыль.')
    print(f"Рентабельность равна: {round((profit / cost * 100), 2)}%")
    personal_count = int(input('Укажите количество сотрудников: '))
    personal_profit = (profit - cost) / personal_count
    print(f'Доход на на одного сотрудника равен: {round(personal_profit,2)}.')
else:
    print(f'В прошедшем квартале вы работали в убыток.')