#1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
#     Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

from collections import Counter
from hashlib import sha1

def count_unic_str(str):

    count = Counter()
    for a in range(len(str)):
        b = a + 1
        while b <= len(str):
            if not (b == len(str) and a == 0):
                data = str[a:b]
                if not data.lstrip() == "":
                    count[sha1(data.encode('utf-8')).hexdigest()] += 1
            b += 1

    l = len(count)
    return l



str = input("строка: ")
print("уникальных строк:", count_unic_str(str))

