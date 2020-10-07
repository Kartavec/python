import json

acum_profit = 0
count = 0
ret = [dict(), dict()]
with open('7.txt', 'r') as f:
    for line in f:
        elements = line.split()

        name = elements[0]
        profit = float(elements[2]) - float(elements[3])
        if profit > 0:
            acum_profit += profit
            count += 1
        ret[0][name] = profit

ret[1]['average_profit'] = acum_profit/count

print(ret)

with open('7.json', 'w') as f:
    json.dump(ret, f)
