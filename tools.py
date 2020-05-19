class IntInputRequiredError(Exception):
    pass


def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        raise IntInputRequiredError('В данном пункте необходимо ввести число')
