time = int(input('Введите время в секундах '))
hours = time // 3600
minutes = (time // 60) % 60
sec = time % 60
print(f'Вы ввели {hours:02}:{minutes:02}:{sec:02}')