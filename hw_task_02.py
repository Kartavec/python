# task 02
# The user enters time in seconds
# then seconds are converted into hours, minutes and seconds
# and are displayed in the hours:minutes:seconds format

time_in_secs = int(input('Please enter time in seconds (not less than 10000): '))

if time_in_secs < 10000:
    time_in_secs = int(input('Please enter time in seconds (not less than 10000): '))

hours = time_in_secs // 3600

minutes = ((time_in_secs - (hours * 3600)) // 60)

seconds = time_in_secs - hours * 3600 - minutes * 60

print('{}:{}:{}'.format(hours, minutes, seconds))


