# input
n = int(input('Введите число: '))
# parser
output = n+int(f"{n}{n}")+int(f"{n}{n}{n}")
# display
print(f"Вывод: {output}")