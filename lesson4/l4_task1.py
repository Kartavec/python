from sys import argv

payroll, hours, rate, award = argv
print(argv)
print((int(hours) * int(rate)) + int(award))