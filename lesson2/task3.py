

seasons = {'winter':[12,1,2], 
            'spring':[3,4,5],
            'summer':[6,7,8],
            'autumn':[9,10,11]}
month = input('Введите номер месяца: ')
if not month.isdigit():
    print('Неверный ввод')
else:
    print(next(k for k,v in seasons.items() if int(month) in v))