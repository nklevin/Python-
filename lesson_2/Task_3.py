month = int(input('Введите месяц по номеру:'))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}

if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])

elif 3 <= month <= 6:
    print(seasons_dict.get(2))
    print(seasons_list[1])

elif 6 < month <= 9:
    print(seasons_dict.get(3))
    print(seasons_list[2])
    
elif 9 < month <= 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
