my_list = [1, 2, 3, 1, 7, 6, 6, 2, 1]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
