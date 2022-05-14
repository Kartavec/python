"""Модуль strings"""

# примеры строк
# переменные, объявленные на уровне модуля являются глобальными (константы
# в верхнем регистре)
FIRST_STR = 'Программирование'
print(FIRST_STR)
print(type(FIRST_STR))
SECOND_STR = 'Programování'
print(SECOND_STR)

print('----------------------------------------------------')
# форматы записи юникод-символов
FIRST_SYMBOL = '\N{LATIN SMALL LETTER C WITH DOT ABOVE}'
print(FIRST_SYMBOL)

SECOND_SYMBOL = '\u010B'
print(SECOND_SYMBOL)

print('----------------------------------------------------')
# строка, как последовательность юникод-символов
FIRST_WORD = 'Программа'
SECOND_WORD = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
print(type(SECOND_WORD))
print(SECOND_WORD)

print(FIRST_WORD == SECOND_WORD)

print(len(SECOND_WORD))

print('----------------------------------------------------')

# 1 конвертор теста в unicode: https://calcsbox.com/post/konverter-teksta-v-unikod.html

# 2 получение кодовой точки путём преобразования десятичного значение символа в шестнадцатеричный
# подробнее здесь:
# https://stackoverflow.com/questions/48556741/what-refers-to-04x-in-python-unicode-characteristics

code_point = rf"\u{'%04x' % ord('€')}"
print('Кодовая точка символа евро (€): ', code_point)

# принцип работы:
# сначала функция ord('€') получает десятичный код символа € = 8364
# затем выражение '%04x' % 8364 даёт шестнадцатеричный код числа 8364, равный 20ac

# 3 получение кодовых точек для НЕ ascii-символов с помощью unicode_escape
text = 'Привет!'.encode('unicode_escape')
print(type(text))
print("'Привет!'.encode('unicode_escape'): ", text)

# ВАЖНО для домашнего задания!!!
# Варианты 2 и 3 не является заменой варианта 1!!!!

print('----------------------------------------------------')
# функция ord позволяет получить числовое значение символа
# в десятичном виде
decimal_code = ord('ã')
print(decimal_code)  # 227

# это косвенный способ определить принадлежность символа к ascii-коду:
# если ord(x) > 127, значит это не ascii-символ!

# функция chr позволяет получить символ по коду
print(chr(227))
