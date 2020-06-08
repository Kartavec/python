# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

from task02 import split_text_by_rows


def get_profits_and_damages(companies):
    profits = {}
    damages = {}
    profit_values = []
    for company in companies:
        name, _, revenue, costs = company.split(' ')

        profit = int(revenue) - int(costs)
        if profit > 0:
            profits[name] = profit
            profit_values.append(profit)
        elif profit < 0:
            damages[name] = profit
    return profits, damages, profit_values


if __name__ == '__main__':
    filename = 'data/task07.txt'
    output_filename = 'output/task07.json'
    companies = split_text_by_rows(filename)
    profits, damages, profit_values = get_profits_and_damages(companies)
    average_profit = sum(profit_values) / len(profit_values)
    result = [profits,
              {"average_profit": average_profit},
              damages]
    with open(output_filename, 'w') as file:
        file.write(json.dumps(result, ensure_ascii=False))
