sum_of_numbers = int(input("Первое число: "))
mult_of_numbers = int(input("Второе число: "))
x = sum_of_numbers // 2
y = sum_of_numbers - x
for i in range(1, 1000):
    if x * y == mult_of_numbers:
        print(f"Задуманные числа: {x}, {y}")
        break
    else:
        print("Не правильно. Попробуй еще раз")
        break
