# input 

v = int(input("Введите вермя в секундах:"))
hours = v//3600
minutes = (v % 3600) // 60
seconds = (v % 3600) % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
