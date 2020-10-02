
def add_and_print(inp_string, sum):
	inp_nums = inp_string.split()
	for elem in inp_nums:
		if elem != 's':
			sum += int(elem)
		else:
			print('sum = ' + str(sum))
			return
	print('sum = ' + str(sum))
	return sum

accum = 0
while True:
	inp_string = input('Enter numbers (s for stop) ')
	res = add_and_print(inp_string, accum)
	if res == None:
		break
	else:
		accum = res