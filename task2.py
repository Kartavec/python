a = int(input('Hello! Please, enter time in seconds.'))
hours = a//3600
min = (a-hours*3600)//60
sec = a-hours*3600-min*60
print (f'Your time in hh:mm:ss format is {hours}:{min}:{sec}') 