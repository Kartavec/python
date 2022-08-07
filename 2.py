# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input("Введите количество секунд: "))
hours = user_seconds // 3600
minutes = (user_seconds - (hours * 3600)) // 60
seconds = user_seconds - (hours * 3600) - (minutes * 60)
print(f"Время в формате чч:мм:сс будет - {hours}:{minutes}:{seconds}")
