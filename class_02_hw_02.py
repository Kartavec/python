# Class 02
# Task 02

some_list = []

len_list = int(input("Enter the number of list elements you would like to have: "))

for el in range(len_list):
    elem = input("Enter a list element: ")
    some_list.append(elem)

print(some_list)

for elem in range(1, len(some_list), 2):
    some_list[elem - 1], some_list[elem] = some_list[elem], some_list[elem - 1]

print(some_list)   



