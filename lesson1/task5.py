
earnings = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
statistics = earnings - costs 
if statistics < 0:
    print(f"Убытки {statistics}")
else:
    print(f"Прибыль {statistics}. Соотношение: {earnings/costs}")
    
    employees = int(input("Введите количество сотрудников: "))
    print(f"Прибыль/сотрудник:{statistics//employees}")

