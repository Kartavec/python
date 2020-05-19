def calculate_time(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


def get_max_digit(number):
    result = 0
    for digit in number:
        if int(digit) > result:
            result = int(digit)
    return result


def get_digits_sum(digit):
    factor = (1 + 11 + 111)
    return digit * factor


def calculate_days(result, target):
    factor = 1.1
    day = 1

    while result < target:
        result = result * factor
        day = day + 1
    return day


def get_profit(revenue, costs):
    profit = (revenue - costs) / revenue
    return profit


def get_profit_by_people(revenue, costs, number_of_people):
    profit_by_people = (revenue - costs) / number_of_people
    return profit_by_people
