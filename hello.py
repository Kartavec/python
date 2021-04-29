time = int(input("Type down your time in seconds:  "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f"time = {hours:02}:{minutes:02}:{seconds:02}")
