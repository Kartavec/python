def int_func(word):
	return word[0].upper() + (word[1:])

words =input('Enter string ').split()

goodwords = [int_func(word) for word in words]

for word in goodwords:
	print(word + ' ', end='')