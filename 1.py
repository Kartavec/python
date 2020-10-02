def user_div(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return
		
a = float(input('Enter a '))
b =float(input('Enter b '))

print(user_div(a, b))