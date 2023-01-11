time = int(input('Введите количество секунд: '))
hour = time // 3600
minute = (time % 3600 ) // 60
second = time % 60
print(f'Точное время: {hour}:{minute}:{second}.')