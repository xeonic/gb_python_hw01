# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import time
# seconds input
while True:
    try:
        seconds = int(input('Input seconds - '))
        if seconds >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')

print(time.strftime('%H:%M:%S', time.gmtime(seconds)))
