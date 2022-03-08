revenue = int(input('Выручка: '))
costs = int(input('Издержки: '))
if revenue > costs:
    print('Финансовый результат: прибыль.')
    profit = revenue - costs
    profitability = profit/revenue
    print(f"Рентабельность выручки: {profitability}")
    employees = int(input('Численность сотрудников: '))
    profit_per_emp = profit / employees
    print(f"Прибыль в расчете на сотрудника: {profit_per_emp}")
else:
    print('Финансовый результат: убыток')
