month = input('Введите месяц в числовом формате: ')
my_dict = {
    1:'Winter', 2:'Winter', 3:'Spring',
    4:'Spring', 5:'Spring', 6: 'Summer',
    7: 'Summer', 8:'Summer', 9:'Autumn',
    10:'Autumn', 11:'Autumn', 12:'Winter'
}
if month.isdigit():
    month = int(month)
    print(my_dict.get(month))
else:
    print('Введите номер месяца от 1 до 12.')

