# Class 05
# Task 07
# A script that uses data from a text file with some financial info:
# company's name, form of ownership, revenue, costs
# The script calculates profit of every company and its average profit
# It also puts this into a dictionary and into a jason file


import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'No average profit. All companies operate without profit.')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit of every company - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'We created a json file with the following content: \n'
          f' {js_str}') 
