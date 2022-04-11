total_hours = {}
with open("text_6.txt", 'r', encoding="utf8") as lessons:
    for line in lessons:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '').replace('(пр)', '').\
            replace('(лаб)', '')
        hours = line.split()[1:]
        total_hours = sum(map(int, hours))
        print(f'Total hours of subject {line.split()[0]}: {total_hours}')
