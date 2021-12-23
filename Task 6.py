klm = int(input('Введите ежедневную дистанцию: '))
result = int(input('Введите искомую дистанцию: '))

day = 0

while  True:
    klm = klm * 1.1
    day = day + 1
    if result < klm:
        print(day)
        break
