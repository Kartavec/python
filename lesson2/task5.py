my_list = [7, 5, 3, 3, 2]

our_int = int (input ('Please, enter the number.\t'))

for i in my_list:
    if b <= my_list [-1]:
        my_list.append (b)
        print (my_list)
        b = int (input ('Please, enter the number.\t'))
    elif b > i:
        my_list.insert (my_list.index(i), b)
        print (my_list)
        b = int (input ('Please, enter the number.\t'))
    elif b == i: 
        my_list.insert (my_list.index(i) + 1, b)
        print (my_list)
        b = int (input ('Please, enter the number.\t'))
    elif b < i and b >= my_list[my_list.index(i)+1]:
        my_list.insert (my_list.index(i) + 1, b)
        print (my_list)
        b = int (input ('Please, enter the number.\t'))
    else: continue