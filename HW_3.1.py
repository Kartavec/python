def my_div():
    a = float(input('indicate 1st number: '))
    b = float(input('indicate 2nd number: '))
    try:
        c = a / b
    except ZeroDivisionError:
        return None
    c = a / b
    return c
print(f'division a on b is {my_div():.2f}')
