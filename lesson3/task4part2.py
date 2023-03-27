def my_func(int, degree):
    i = 0 
    res = 1 
    while i != degree:
        i -= 1
        res /= int
    return res

print(my_func(10, -4))