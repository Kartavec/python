def my_func(a, b, c):
	if a < b and a < c:
		return b + c
	elif c < b:
		return a + b
	else :
		return a + c

a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))

print('Sum of the two biggest = ' + str(my_func(a,b,c)))