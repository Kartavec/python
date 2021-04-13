ratings = [9,5,4,4,2,1]
rate = int(input("Рейтинг: "))
ratings.append(rate)
ratings.sort()
ratings.reverse()
print(ratings)