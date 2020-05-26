def parse_string(numbers_in_string):
    numbers = numbers_in_string.split()
    return numbers


def summarize(summary, numbers):
    for number in numbers:
        try:
            summary = summary + int(number)
        except ValueError:
            status = 0
            return summary, status
    status = 1
    return summary, status


def main():
    summary = 0
    status = 1
    while status == 1:
        input_string = input('Введите числа, разделённые пробелами: ')

        numbers = parse_string(input_string)

        summary, status = summarize(summary, numbers)

        print(summary)


if __name__ == '__main__':
    main()
