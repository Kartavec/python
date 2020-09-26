goods = []

num = 1
while True:
    inp = input('Enter new element or stop ')
    if inp.lower() == 'stop':
        break
    cost = input('Enter cost ')
    count = input('Enter count ')
    unit = input('Enter unit ')
    goods.append(tuple([num, {'name': inp, 'cost': cost, 'count': count, 'unit': unit}]))
    num += num

names_set = set()
costs_set = set()
counts_set = set()
units_set = set()

for good in goods:
    names_set.add(good[1]['name'])
    costs_set.add(good[1]['cost'])
    counts_set.add(good[1]['count'])
    units_set.add(good[1]['unit'])

goods_info = {'name': names_set, 'cost': costs_set, 'count': counts_set, 'unit': units_set}
print(goods_info)
