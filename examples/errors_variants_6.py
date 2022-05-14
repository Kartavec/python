"""
Модуль errors_variants
"""

SOME_STR = 'Testování'
# ошибка - преобразование в байты
print(SOME_STR.encode('ascii'))

print('----------------------------------------------------')
# ошибка - строку, преобразованную в байты в кодировке utf-8
# преобразуем в строку в кодировке ascii
some_str_bytes = SOME_STR.encode('utf-8')
new_str = some_str_bytes.decode('ascii')
print(new_str)

print('----------------------------------------------------')
# ошибка - разные кодировки для преобразований
some_str_bytes = SOME_STR.encode('utf-16')
new_str = some_str_bytes.decode('utf-8')
print(new_str)
