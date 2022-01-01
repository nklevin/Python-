def salary():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка: '))
        bonus = int(input('Премия: '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника - {res}')
    except ValueError:
        return print('Not a number')
salary()
