# Class 03
# Task 05
# A simple function that takes a string of several numbers
# separated by spaces and prints sum of  those numbers when Enter is pressed.
# The user can proceed and enter a string of several numbers separated by spaces again.
# The sum of number in the new string is added to the previous sum.

def sum_nums_in_string():
    s = 0
    try:
        while True:
            for n in map(int, input("Enter a string of several numbers separated by spaces: ").split()):
                s += n
            print(s)
    except ValueError:
        print(s)

sum_nums_in_string()
            
  
