rating = [9, 7, 5, 3, 1]
print(rating)
while True:
    inp = input('Enter new rating or stop ')
    if inp.lower() != 'stop':
        new_elem = int(inp)
    else:
        break

    pos = 0

    for elem in rating:
        if new_elem >= elem:
            rating.insert(pos, new_elem)
            break

        pos += 1
    else:
        rating.insert(pos, new_elem)

    print(rating)
