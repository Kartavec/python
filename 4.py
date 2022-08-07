# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число "))
final_max = 0
while number != 0:
    current_number = number % 10
    if final_max < current_number:
        final_max = current_number
    number = number // 10
print(f"Максимальная цифра во введенном числе: {final_max}")
