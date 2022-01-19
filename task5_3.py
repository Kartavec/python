import random


def get_jokes(number,origin):
    for _ in range(number):
        if origin == 1:  # diversity flag
            if len(adverbs) == 0 or len(nouns) == 0 or len(adjectives) == 0:
                print("Пардон, шутки закончились(((")
                break

            print(f"{nouns.pop(random.randint(0, len(nouns)-1))} "
                f"{adverbs.pop(random.randint(0, len(adverbs) - 1))} "
                f"{adjectives.pop(random.randint(0, len(adjectives) - 1))}")
        else:
            print(f"{nouns[random.randint(0, len(nouns) - 1)]} "
                  f"{adverbs[random.randint(0, len(adverbs) - 1)]} "
                  f"{adjectives[random.randint(0, len(adjectives) - 1)]}")

# non-humorous jokes.
nouns = ["автомобиль", "лес", "огонь", "город", "лист", "колобок"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "послезавтра"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "зелёновый"]

get_jokes(int(input("Enter Jokes Number: ")),
          int(input("Without repeat? (y = 1/n = 0): ")))
