# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:

# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# first day
while True:
    try:
        first = int(input('Input first day distance - '))
        if first >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')
# target
while True:
    try:
        target = int(input('Input target - '))
        if target >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')
# day counter
cnt = 1
while True:
    f_str = '{:.3g}'.format(first)
    print(f'{cnt}-й день: {f_str}')
    if first > target:
        break
    cnt += 1
    first = first + first * 0.1

# print result
print(f'Ответ: на {cnt}-й день спортсмен достиг результата — не менее {target} км.')
