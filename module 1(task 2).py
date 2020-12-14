# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

random_sec = int(input("Введите время в секундах "))

hours = random_sec // 3600
minutes = (random_sec - hours*3600) // 60
seconds = random_sec - (hours*3600 + minutes*60)

print(f"{hours:02}:{minutes:02}:{seconds:02}")
