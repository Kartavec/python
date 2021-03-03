# Class 02
# Task 03

# Solution 1

seasons = ['winter', 'spring', 'summer', 'autumn']

month_num = int(input('Choose a month (1-12): '))

if month_num == 1 or month_num == 2 or month_num == 12:
    print('It is', seasons[0], '!')

elif month_num == 3 or month_num == 4 or month_num == 5:
    print('It is', seasons[1], '!')

elif month_num == 6 or month_num == 7 or month_num == 8:
    print('It is', seasons[2], '!')

elif month_num == 9 or month_num == 10 or month_num == 11:
    print('It is', seasons[3], '!')

else:
    print('Error! You need to enter number from 1 to 12!')


# Solution 2
 
seasons = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
 
month = int(input('Choose a month (1-12): '))
for key in seasons.keys():
    if month in seasons[key]:
        print('It is', key.lower(), '!')
        
