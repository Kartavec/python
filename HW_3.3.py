def my_func():
    a = float(input('print 1st number '))
    b = float(input('print 2nd number '))
    c = float(input('print 3rd number '))
    value_list = [a, b, c]
    value_list.pop(value_list.index(min(value_list)))
    max_sum = sum(value_list)
    return max_sum
print(f'the sum of the bigest 2 numbers given by you is {my_func()}')