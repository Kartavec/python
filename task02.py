# Создать текстовый файл (непрограммно), сохранить в
# нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


def split_text_by_rows(filename):
    with open(filename) as file:
        p = file.read()

    result = p.split('\n')

    return result


def count_words_in_row(row):
    words = row.split(' ')
    if words[0] == '':
        return 0
    else:
        return len(words)


def print_count_of_words_in_rows(rows):
    for row in enumerate(rows, start=1):
        row_number, row_text = row
        print(f'{row_number} - {count_words_in_row(row_text)}')


if __name__ == '__main__':
    input_file = 'task02.txt'
    rows = split_text_by_rows(input_file)

    print(f'Количество строк в текста - {len(rows)}.')
    print('Количество слов в строках:')
    print_count_of_words_in_rows(rows)
