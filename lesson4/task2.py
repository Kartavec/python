my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        new_list.append(my_list[i])
print(new_list)
