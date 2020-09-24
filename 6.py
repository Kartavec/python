import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

save_a = a

day = 0
while a < b:
    a = a * 1.1
    day += 1

print(f'Первый день {save_a} км, результат {b} км будет достигнут через {day} дней')