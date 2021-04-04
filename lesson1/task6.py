
start_res = int(input("Начальный результат: "))
target_res = int(input("Целевой результат: "))
days = 1 
while start_res < target_res:
    start_res*=1.1
    days+=1
print(f'Достижение результата в течение {days} дней')