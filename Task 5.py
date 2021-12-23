income = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))

if income > costs:
    print('Фирма прибыльна')
    print(f'Рентабельность фирмы:{int( ( (income - costs) / income) * 100)} %')
    staff = int(input(('Введите число сотруднков:')))
    print(f'Прибль на сотрудника:{int((income - costs) / staff)}')
else:
    print('Фирма убыточна')

