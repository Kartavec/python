
# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input("Введите число 'n' для операции: "))
num_sum = (num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))
print("Сума n + nn + nnn будет: ", num_sum)
