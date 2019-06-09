import math
import timeit
import cProfile

def eratosfen(i):

    # Первый проход - 100

    currentmin = 2

    mas = []

    def _clening(mas):

        for pos, i in enumerate(mas):
            if i == 0:
                continue
            for a in range(pos + 1, len(mas)):
                if mas[a] != 0 and mas[a] % i == 0:
                    mas[a] = 0

    def _getnum(mas, i):

        cur = 0
        for a in mas:
            if a != 0:
                cur += 1
            if cur == i:
                return a

        return None


    num = None
    while num is None:

        currentmax = currentmin + 100
        mas += [i for i in range(currentmin, currentmax)]
        _clening(mas)
        num = _getnum(mas, i)
        currentmin = currentmax

    return num

def simple(i):

    def _issimple(val):

        limit = int(math.sqrt(val))
        i = 2
        while i <= limit:

            if val % i == 0:
                return False
            i += 1

        return True

    val = 2
    curnum = 0
    while True:

        if _issimple(val):
            curnum += 1
            if curnum == i:
                return val

        val += 1


i = int(input("Номер числа: "))
rez = eratosfen(i)

print("Результат эратосфен: ", rez)

NUMBER = 3

cProfile.run("eratosfen(i)")

print("Время эратосфен:", timeit.timeit("eratosfen(i)", number=NUMBER, globals=globals()) / NUMBER)

# 100е число: 440 function calls in 0.007 seconds
# 200е число: 1641 function calls in 0.056 seconds
# 300е число: 3514 function calls in 0.181 seconds
# 400е число: 6427 function calls in 0.465 seconds
# 500е число: 10129 function calls in 1.033 seconds

rez = simple(i)

print("Результат перебор: ", rez)

cProfile.run("simple(i)")

print("Время перебор:", timeit.timeit("simple(i)", number=NUMBER, globals=globals()) / NUMBER)

# 100е число: 1084 function calls in 0.001 seconds
# 200е число: 2448 function calls in 0.001 seconds
# 300е число: 3976 function calls in 0.002 seconds
# 400е число: 5484 function calls in 0.004 seconds
# 500е число: 7144 function calls in 0.005 seconds

# ВЫВОДЫ:
# 1. РЕШЕТО ЭРАТОСФЕНА для поиска n-го числа неэффективно, т.к фактически сложность равна
# O(n**3) - мы имеем 3 вложенных цикла. Замеры подтверждают, что время выполнения растет намного быстрее
# чем растет индекс элемента которого надо найти (фактически размерность входного макссива)
# 2. Во втором варианте имеем почти линейный рост, что опять же ожидаемо, т.к нам нужно перебрать просто больше
# элементов что бы найти следующий. Т.е сложность О(n). "почти линейный рост" - потому что на больших числах
# _issimple все таки будет работать медленне чем на малых, т.к нужно перебрать больше составляющих