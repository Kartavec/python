my_list = []
element = ''
elem_index = 0
i = 1

#заполняем список
while element != 'quit':
    my_list.append (input (f'Enter the {i} element of list, please.\t'))
    element = my_list [-1]
    i += 1
del my_list [-1]

# определяем четное или нечетное количетсво элементов в списке
# и меняем местами соседние элементы
if len (my_list) % 2 == 0:
    while elem_index <= len (my_list) - 2:
        my_list [elem_index], my_list [elem_index + 1] = my_list [elem_index + 1], my_list [elem_index]
        elem_index += 2
else:   
    while elem_index < len (my_list) - 2:
        my_list [elem_index], my_list [elem_index + 1] = my_list [elem_index + 1], my_list [elem_index]
        elem_index += 2

print (my_list)


