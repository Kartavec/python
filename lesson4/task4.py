my_list = [1, 1, 24, 44, 67, 74, 74, 7, 9, 74, 245, 66, 9, 88]
new_list = []

generator = (numb for numb in my_list if my_list.count(numb) == 1)
for i in generator:
    new_list.append(i)
print(new_list)
