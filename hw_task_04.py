# task 04
# The user enters any 3-digit positive interger n.
# This simple program defines the biggest digit in the integer.

num = int(input('Enter any 3-digit number: '))

list_of_digits = []

while num > 10:
    list_of_digits.append(num % 10)
    num //= 10

biggest_digit = max(list_of_digits)

print(biggest_digit)
    


