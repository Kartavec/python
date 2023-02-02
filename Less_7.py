# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка будет содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
# прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

m_file = open('text_6.txt', 'r', encoding='utf-8')
lines = m_file.read().splitlines()
d_1 = {}
sum_rev = 0
num_f = 0
for item in lines:
    key = item.split(' ')[0]
    ls = item.split(' ')[2:]
    value = int(ls[0]) - int(ls[1])
    d_1.update({key: value})
    sum_rev += value
    num_f += 1

d_2 = {}
key_2 = 'average_profit'
value_2 = sum_rev / num_f
d_2.update({key_2: value_2})
res = [d_1, d_2]
print(res)
