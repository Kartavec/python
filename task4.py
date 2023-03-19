number = input('Please, enter positive integer.\n')
max = 0
for i in number:
    i = int(i)
    if i > max:
        max = i
print (f'The largest number in your integer is {max}.')        
