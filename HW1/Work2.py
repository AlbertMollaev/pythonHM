x = 2
y = 3
S = x + y
P = x * y
print("Загадали два числа, сумма и произведение которых равна: ", S, "и", P, ".", "Какие два числа были загаданы?")
i = 0
count_number = 10
while i <= count_number:
    first_number = int(input("Первое число: "))
    second_number = int(input("Второе число: "))
    if first_number == x and second_number == y:
        print(S, P, "->", first_number, second_number)
        break
    else:
        print("Не правильно, попробуй еще раз. Осталось попыток угадать: ", count_number)
    count_number -= 1
    i += 1