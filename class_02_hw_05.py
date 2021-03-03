# Class 02
# Task 05

some_list = [8, 7, 5, 4, 4, 3, 1, 1]

new_num = int(input("Enter a new number: "))

coun = some_list.count(new_num)

for element in some_list:
    if coun > 0:
        i = some_list.index(new_num)
        some_list.insert(i+coun, new_num)
        break
    else:
        if new_num > element:
            j = my_list.index(element)
            some_list.insert(j, new_num)
            break
        elif new_num < some_list[len(some_list) - 1]:
            some_list.append(new_num)
            
print(some_list) 
    

                    
