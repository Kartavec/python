#задание 1
i = int(input('введите число:'))
n = input('введите что нибудь:')
st = str(input('введите строковое:'))
fl = float(input('введите float:'))

print(1,n,st,fl)
print('целое',type(i),i)
print('класс присвоился автоматически',type(n),n)
print('строка',type(st),st)
print('с запятой',type(fl),fl)

print ('целое + строка',str(i)+st)


# задание 2
n = int(input('введите время в секудах:'))
h = n//3600
m = (n-(h*3600))//60
s = n-h*3600-m*60
print (h,':',m,':',s)

# задание 3
f=str(input('ведите число, а его сложу:'))
p=f+f
l=f+f+f
o=int(f)+int(p)+int(l)
print(o)

# fзадание 4
t = int(input('целое число, а я найду самую большую цифру'))
x: int = 0
c = None
while t > 0:
    c = t % 10
    t = t // 10
    if x < c:
        x = c
        continue
print('x=', x)

# задание 5,6
t = int(input('выручка?'))
z = int(input('издержки?'))
if (t-z) > 0:
    print ('фирма отработала с прибылью',(t-z))
    v = int(input('число сотрудников?'))
    print ('рентабельность средняя на сотрудника', (t-z)/v)
elif (t-z) == 0:
    print ('фирма отработала в ноль')
elif (t-z)< 0:
    print ('фирма отработала с убытком', (t-z))

#задание 7
start=int(input('начальный километраж бегуна'))
end = int(input('нужно достич километраж '))
day : int = 1
print(day, '- день :', start)
while end > start:
    start = round((start * 1.1),2)
    day += 1
    print(day,'- день :',start)
print('на',day,'- день будет пробегать не менее:',end, 'км')
# изучение git4