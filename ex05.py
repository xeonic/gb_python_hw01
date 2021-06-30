# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# earnings
while True:
    try:
        earnings = int(input('Input earnings - '))
        if earnings >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')
# costs
while True:
    try:
        costs = int(input('Input costs - '))
        if costs >= 0:
            break
        else:
            print('Input positive number')
    except ValueError:
        print('Input number!')

if earnings > costs:
    print('The company works for profit')
    print(f'Profitability is {earnings / costs}')
    # employee count
    while True:
        try:
            count = int(input('Input employee count - '))
            if count >= 0:
                break
            else:
                print('Input positive number')
        except ValueError:
            print('Input number!')
    print(f'Earnings per employee is {earnings / count}')
else:
    print('The company works for loss')

