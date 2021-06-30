# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    try:
        num = int(input('Input positive number - '))
        if num >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')

max_num = 0

while num / 10 > 0:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10

print(f'maximum digit is: {max_num}')
