my_list = [300, 5, 1, 5, 7, -1, 0]
new_list = []
for i in range(len(my_list) - 1):
    n = my_list[i]
    i += 1
    m = my_list[i]
    if m > n:
        new_list.append(m)
print(new_list)