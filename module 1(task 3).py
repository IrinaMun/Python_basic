# Узнайте у пользователя число n.
# #Найдите сумму чисел n + nn + nnn.

n = int(input("Введите число "))

nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))

summa = n + nn + nnn

print(summa)

