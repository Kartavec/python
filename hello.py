num = int(input("Type your positive integer number: "))
n = num
max = n % 10
while n:
    i = n % 10
    if i > max:
        max = i
    n = n // 10
print(f'The greatest figure in the number is {max} ')