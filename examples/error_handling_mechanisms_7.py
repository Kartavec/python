"""
Модуль error_handling_mechanisms
"""


SOME_STR = 'Testování'

print('===== Кодирование =====')
# обработка ошибки кодирования с заменой символа знаком вопроса
new_str = SOME_STR.encode('ascii', 'replace')
print('replace: ', new_str)

print('----------------------------------------------------')
# обработка ошибки кодирования с заменой символа его именем
new_str = SOME_STR.encode('ascii', 'namereplace')
print('namereplace: ', new_str)

print('----------------------------------------------------')
# игнорирование ошибки при кодировании
new_str = SOME_STR.encode('ascii', 'ignore')
print('ignore: ', new_str)

# игнорирование ошибки при кодировании
new_str = SOME_STR.encode('ascii', 'xmlcharrefreplace')
print('xmlcharrefreplace: ', new_str)

print('===== Декодирование =====')
# создаём тестовое значение
SOME_STR_BYTES = SOME_STR.encode('utf-8')
print(SOME_STR_BYTES)

print('----------------------------------------------------')
# игнорирование ошибки при кодировании
new_str = SOME_STR_BYTES.decode('ascii', 'ignore')
print('ignore: ', new_str)

print('----------------------------------------------------')
# замена ошибки при декодировании
new_str = SOME_STR_BYTES.decode('ascii', 'replace')
print('replace: ', new_str)


# какой вариант лучше?
