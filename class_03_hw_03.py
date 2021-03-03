# Class 03
# Task 03
# A simple function that takes 3 positional args
# and returns the sum of 2 biggest args.

def my_func(a, b, c):
    if a >= b and c >= b:
        return a + b
    
    elif b >= a and c >= a:
        return b + c

    else:
        return a + c


a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
c = int(input("Enter an integer: "))
        

print(my_func(a, b, c))



    
        

    
    
        
    
