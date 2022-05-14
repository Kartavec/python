"""
Модуль file_system
"""

from chardet import detect

# --- 1. создаём файл в заданной кодировке
f = open('test.txt', 'w', encoding='utf-8')
f.write('тест тест тест')
f.close()


# --- 2. узнаём кодировку (как будто бы!) неизвестного нам файла
with open('test.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)


# --- 3. Теперь открываем файл в УЖЕ известной нам кодировке
with open('test.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()
