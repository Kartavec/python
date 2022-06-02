def int_func(word):
    # Можно использовать title :)
    # return word.title()
    return word[0].upper() + word[1:]


# Task 6
print(int_func('text'))

# Task 7
words = input('Введите строку: ').split()
print(*[int_func(w) for w in words])
