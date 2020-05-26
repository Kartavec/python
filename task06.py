import re


def check_for_lower_and_latin_letter(string):
    template = r'^([a-z]+\s)*[a-z]+$'
    if re.search(template, string):
        return True
    return False


def upper_first_letter_in_word(word):
    result = word[0].upper() + word[1:]
    return result


def upper_first_letter_in_words(words):
    upper_words = []
    for word in words.split():
        word = upper_first_letter_in_word(word)
        upper_words.append(word)
    result_string = ' '.join(upper_words)
    return result_string


def main():
    input_string = input('Введите строку из слов, состоящих из латинских букв в нижнем регистре,'
                         ' и  разделенных пробелом: ')

    if not check_for_lower_and_latin_letter(input_string):
        print('Необходимо ввести строку из слов, состоящих из латинских букв в нижнем регистре!')
        return

    result = upper_first_letter_in_words(input_string)
    print(result)


if __name__ == '__main__':
    main()
