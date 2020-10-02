def neg_pow(a, b):
	if b >= 0:
		return
	b = -b
	ret = 1
	for i in range(0, b):
		ret /= a
	return ret

a = float(input('Enter a '))
b = int(input('Enter b '))

print('a**b = ' + str(neg_pow(a,b)))