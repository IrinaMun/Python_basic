# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.

user_number = int(input("Введите целое положительное число "))

max_number = user_number % 10
user_number = user_number // 10

while user_number > 0:
    n = user_number % 10

    if max_number < n:
        max_number = n

    user_number = user_number // 10


print("Самая большая цифра в числе ", max_number)
