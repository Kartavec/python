number = input('Please, enter positive integer.\n')
max_number = 0

for i in number:
    i = int(i)
    if i > max_number:
        max_number = i

print (f'The largest number in your integer is {max_number}.')