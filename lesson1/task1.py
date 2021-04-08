# variables
var1:int
var2:str 
# input
inputted_vars = input('Введите переменные через запятую: ').split(',')
# parser
var1 = int(inputted_vars[0])
var2 = inputted_vars[1]
# display
print(f'Переменная 1 (Целое число) {var1} {type(var1)}')
print(f'Переменная 2 (Строка) {var2} {type(var2)} ')