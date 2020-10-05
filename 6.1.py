from itertools import count


def whole_nums(first_num):
    for elem in count(first_num):
        if elem > 100:
            break
        yield elem


print(list(whole_nums(5)))

