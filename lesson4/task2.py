my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

my_generator = (numb for numb in my_list[1:] if numb > my_list[my_list.index(numb)-1])
for i in my_generator:
    new_list.append(i)
print(new_list)