result = int(input('Введите результат первого дня: '))
goal = int(input('Цель: '))
day_number = 1
while result < goal:
    result = result + (result / 100 * 10)
    day_number = day_number + 1
print(f"На {day_number} день спортсмен достиг результата не менее {goal} км")
