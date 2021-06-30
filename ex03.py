# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    try:
        num = int(input('Input positive number - '))
        if num >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')

print(num * 100 + num * 10 * 2 + num * 3)
