my_list = input('введите строку чисел, разделенных пробелом ')
my_list = list(my_list)
d = sum(map(int, ' '.join(my_list).split()))
print(d)