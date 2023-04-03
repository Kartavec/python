my_list = [1, 'hello',  [1, 3, 5],  (1, 2, 3, 4), {'key' : 'meaning'}]

for i in my_list:
    data_type = type (i)
    print (f'Data type of {my_list.index(i)} element of my list is {data_type}.')
