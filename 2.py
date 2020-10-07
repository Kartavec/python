with open('2.txt', 'r', encoding='utf-8') as f:
    lines_count = 0
    for line in f:
        words = line.split()
        print(f'{len(words)} lines in line #{lines_count}')
        lines_count += 1


    print(f'Overall lines: {lines_count}')
 