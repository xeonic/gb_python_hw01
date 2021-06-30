# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

import datetime
# Name
name = input('Input your name - ')

# Sex
while True:
    sex = input('Input sex M/F - ')
    if sex != 'M' and sex != 'F':
        print(f"{sex} isn't a correct sex")
    else:
        break
# Age
while True:
    try:
        age = int(input('Input age - '))
        if age >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')

# City
city = input('Input birth city - ')

print(f'{name} was born in {city} in {datetime.datetime.now().year - age}')
