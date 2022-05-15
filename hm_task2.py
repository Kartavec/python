def check_data(word):
    print("Type :", type(word), "Content :", word, "Length :", len(word))


if __name__ == "__main__":
    words_bank = [b"class", b"function", b"method"]
    for i in words_bank:
        check_data(i)
