# input 
v = int(input('Введите число: '))
# variable
max_val = 0
# solver
while v>0:
    prob=  v%10
    if prob > max_val:
        max_val = prob
    v=v//10
print(max_val)