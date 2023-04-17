import json
with open('task7text.txt', 'r') as file_object:
    data = file_object.readlines()
dict_profit = {}
list_profit = [] 
sum_profit = 0
print(data)
for i in data:
    i = i.replace("\n", "")
    company = i.split()
    company_name = company[0]
    profit = int(company[2])
    costs = int(company[3])
    dict_profit[company_name] = profit - costs
    if (profit - costs) > 0:
        sum_profit += (profit - costs)
av_profit = sum_profit / len(data)
av_profit = round(av_profit, 1)
dict_profit['average_profit'] = av_profit
list_profit.append(dict_profit)
print(list_profit)
list_profit = json.dumps(list_profit)
with open('task7jsonfile.json', 'w') as file_object:
    file_object.write(list_profit)
