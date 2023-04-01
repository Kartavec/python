def factorial_func(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result
n = int(input('Please, enter N.\t'))
for j in factorial_func(n):
    print(j)