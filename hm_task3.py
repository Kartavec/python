def check_var1(word):
    try:
        bytes(word, encoding='ascii')
    except UnicodeEncodeError:
        print(word, "cannot be transformed to bytes")


def check_var2(word):
    array_errors = [x for x in word if ord(x) > 127]
    if len(array_errors) > 0:
        print(word, "cannot be transformed to bytes")


words_bank = ["attribute", "класс", "функция", "type"]
print("var 1:")
for i in words_bank:
    check_var1(i)
print("\nvar 2:")
for i in words_bank:
    check_var2(i)
