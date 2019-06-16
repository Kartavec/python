# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import deque

def test(digit1, digit2):
    a = int(digit1, 16)
    b = int(digit2, 16)
    a += b
    return  hex(a)

HexData = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

firstdig = input("first digit: ").upper()
seconddig = input("second digit: ").upper()

test = test(firstdig, seconddig).upper()
print("Проверка: ", test)


firstdig = list(firstdig)
seconddig = list(seconddig)

deq = deque([i for i,v in HexData.items()], maxlen=16)

if len(firstdig) < len(seconddig):
    firstdig, seconddig = seconddig, firstdig

rezult = deque()
isRaz = 0

for i in range(len(firstdig)):

    cur = len(firstdig) - i - 1
    curdec = deq.copy()
    ind1 = HexData[firstdig[cur]]
    curdec.rotate(-ind1)
    ind2 = 0
    if i < len(seconddig):
        cur = len(seconddig) - i - 1
        ind2 = HexData[seconddig[cur]]
        curdec.rotate(-ind2)
    curdec.rotate(-isRaz)
    rezult.appendleft(curdec[0])
    isRaz = ind1 + ind2 + isRaz >= deq.maxlen

if isRaz:
    rezult.appendleft("1")

rezult = "".join(rezult)
print("Результат: ", rezult)
print("Проверка: ", "все сошлось" if "0X" + rezult == test else "ошибка")