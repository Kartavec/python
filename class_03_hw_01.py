# Class 03
# Task 01
# A simple function that takes 2 numbers as positional args.
# The function returns the number obtained by dividing one arg by another arg.

def quotient(f_num, s_num):
    try:
        answer = int(f_num) / int(s_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
print("Give me 2 numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nEnter the first number: ")
    if first_num == 'q':
        break
    second_num = input("\nEnter the second number: ")

    quotient(first_num, second_num)

    
    
        





