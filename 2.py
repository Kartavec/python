
length = int(input('Enter list length '))

my_list = []
for i in range(0, length):
    my_list.append(input('Enter new element of list '))

for i in range(0, length - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)