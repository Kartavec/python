season_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer',
               'Autumn', 'Autumn', 'Autumn', 'Winter']
season_dict = {'1': 'Winter', '2': 'Winter', '3': 'Spring', '4': 'Spring', '5': 'Spring', '6': 'Summer',
               '7': 'Summer', '8': 'Summer', '9': 'Autumn', '10': 'Autumn', '11': 'Autumn', '12': 'Winter'}

month_num = input('Enter month number ')

list_month_num = int(month_num) - 1

if list_month_num < 0 or list_month_num > 11:
    print('Wrong month number')
else:
    print(f'Season from list: {season_list[list_month_num]}')

    print(f'Season from dict: {season_dict[month_num]}')
