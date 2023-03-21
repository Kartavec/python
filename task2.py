a = int(input('Hello! Please, enter time in seconds.\t'))

hours = a // 3600
minutes = (a - hours * 3600) // 60
seconds = a - hours * 3600 - minutes * 60

print(f'Your time in hh:mm:ss format is {hours}:{minutes}:{seconds}')