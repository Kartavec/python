from task01 import write_to_file
from task02 import split_text_by_rows


def convert_eng_to_rus(eng_number):
    if eng_number == 'One':
        return 'Один'
    elif eng_number == 'Two':
        return 'Два'
    elif eng_number == 'Three':
        return 'Три'
    elif eng_number == 'Four':
        return 'Четыре'


def convert_row(row):
    eng, number = row.split(' — ')
    rus = convert_eng_to_rus(eng)
    return f'{rus} - {number}'


if __name__ == '__main__':
    filename = 'data/task04.txt'
    output_filename = 'output/task04.txt'
    rows = split_text_by_rows(filename)
    for row in rows:
        rus_row = convert_row(row)
        write_to_file(output_filename, rus_row, 'a')