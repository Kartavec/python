import itertools
my_list = [1, 1, 24, 44]
reiteration = int(input('How many times do you want to print the list?\t'))
count = 0
for i in itertools.cycle(my_list):
    print(i, end=' ')
    count += 1
    if count == (len(my_list) * reiteration):
        break
