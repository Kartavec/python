"""
Задание 6.
Реализовать функцию int_func(), принимающую слова из маленьких латинских
букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
"""


def int_func(*args):
    return ' '.join([word.title() for word in args])


print(int_func('car', 'world', 'sun'))
