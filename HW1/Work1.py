n = int(input("Введите число монеток которые лежат на столе: "))
heads = 0
tails = 0
for i in range(n):
    x = int(input("Если Орел введите 1, если Решка введите 0: "))
    if x == 1:
        heads += 1
    else:
        tails += 1
print("Колличество монет которые нужно перевернуть :", tails)