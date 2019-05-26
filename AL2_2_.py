nat = int(input('Enter nature number:'))

ch = nch = 0

while nat > 0:
    if nat % 2 == 0:
        ch +=1
    else:
        nch +=1
    nat = nat // 10
print(f'even - {ch}\nodd - {nch}')