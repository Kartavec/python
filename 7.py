def factorial(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
        yield ret


print([el for el in factorial(5)])
