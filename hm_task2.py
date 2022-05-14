def check_data(word):
    print("Type :", type(word), "Content :", word, "Length :", len(word))


words_bank = [b"class", b"function", b"method"]
for i in words_bank:
    check_data(i)
