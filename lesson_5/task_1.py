# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего .

from collections import Counter

comp_count = int(input("Количество компаний: "))

comp_gain = Counter()

gain = 0
for i in range(comp_count):
    name = input("Название компании: ")
    for a in range(4):
        comp_gain[name] += int(input(f"\tВыручка за {(a+1)}кв.: "))
    comp_gain[name] = comp_gain[name] / 4
    gain += comp_gain[name]

gain = gain / comp_count
print("Средняя выручка: ", gain)

maxgain = Counter({k:v for k,v in comp_gain.items() if v >= gain})
print("Больше среднего: ", maxgain)
print("Меньше среднего: ", comp_gain - maxgain)


