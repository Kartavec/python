valid_input = False
while not valid_input:
    try:
        time_sec = int(input('Введите время в секундах: '))
        valid_input = True
    except ValueError:
        print('Секунды должны быть числом! Повторите ввод')

hours = time_sec//3600
minutes = (time_sec-(hours*3600))//60
seconds = time_sec - hours*3600 - minutes*60

print('Время: %02d:%02d:%02d' % (hours, minutes, seconds))
