from functools import reduce


def multiply_elements(elem, next_elem):
    return elem * next_elem


even_list = [num for num in range(100, 1001) if (num % 2) == 0]

print(reduce(multiply_elements, even_list))
