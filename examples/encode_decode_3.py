"""Модуль encode_decode"""

print('======================== 1 способ ==========================')
# простое кодирование - encode
ENC_STR = 'Кодировка'
print(type(ENC_STR))
ENC_STR_BYTES = ENC_STR.encode('utf-8')
print(ENC_STR_BYTES)

print('----------------------------------------------------')
# простое декодирование - decode
DEC_STR_BYTES = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'
print(type(DEC_STR_BYTES))
DEC_STR = DEC_STR_BYTES.decode('utf-8')
print(DEC_STR)

print('======================== 2 способ ==========================')
print('----------------------------------------------------')
# метод encode для класса str (кодировка указана как ключевой аргумент)
ENC_STR = 'Программа'
print(ENC_STR)
ENC_STR_BYTES = str.encode(ENC_STR, encoding='utf-8')
print(ENC_STR_BYTES)

print('----------------------------------------------------')
# метод decode для класса bytes (кодировка указана как ключевой аргумент)
BYTES_OBJ = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
print(type(BYTES_OBJ))
BYTES_DEC = bytes.decode(BYTES_OBJ, encoding='utf-8')
print(BYTES_DEC)

print('======================== 3 способ ==========================')
print('----------------------------------------------------')
# кодирование с помощью функции bytes()
ENC_STR = 'Привет!'
print(type(ENC_STR))
ENC_STR_BYTES = bytes(ENC_STR, encoding='utf-8')
print(ENC_STR_BYTES)

print('----------------------------------------------------')
# метод decode для класса bytes (кодировка указана как ключевой аргумент)
BYTES_OBJ = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
print(type(BYTES_OBJ))
BYTES_DEC = str(BYTES_OBJ, encoding='utf-8')
print('BYTES_DEC=', BYTES_DEC, type(BYTES_DEC))
BYTES_DEC2 = str(BYTES_OBJ)
print('BYTES_DEC2=', BYTES_DEC2, type(BYTES_DEC2))
