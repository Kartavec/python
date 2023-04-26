months = {'12' : 'winter', '1' : 'winter', '2' : 'winter', '3' : 'spring', '4' : 'spring', '5' : 'spring',
          '6' : 'summer', '7' : 'summer', '8' : 'summer', '9' : 'autumn', '10' : 'autumn', '11' : 'autumn'
         }  

month_number = input ('Please, enter the month number.\t')

for i in months.keys():
    if month_number == i:
        print (f'Your month is in {months[i]}.')        
