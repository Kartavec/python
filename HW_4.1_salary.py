from sys import argv

script_name, hours, rate, bonus = argv
print('script name: ', script_name)
print('number of working hours: ', float(hours))
print('salary rate: ', float(rate))
print('bonus: ', float(bonus))

sal_month = hours * rate + bonus
print(f'monthly remuniration is {sal_month}')
