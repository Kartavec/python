"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
1.до минуты: <s> сек;
2.до часа: <m> мин <s> сек;
3.до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

q = 1

while q != 0:
    duration = int(input('Input epoch in seconds or \'0\' to exit : '))
    
    if duration != 0:
        days = duration // 86400  # From epoch to day.
        hours = duration // 3600 % 24  # From epoch to hour
        minutes = duration // 60 % 60  # From epoch to minutes, excluding seconds
        seconds = duration % 60  # From epoch to seconds

        if days:
            print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
        elif hours:
            print(f'{hours} час {minutes} мин {seconds} сек')
        elif minutes:
            print(f'{minutes} мин {seconds} сек')
        else:
            print(f'{seconds} сек')
            duration = int(input('Input epoch in seconds: '))
    else:
        q = 0
