file = "task1.txt"


while True:
        user_input = input('Введите данные: ')
        if not user_input:
            break

        try:
            with open(file, 'a', encoding='utf-8') as d:
                d.write(f'{user_input}\n')

        except IOError:
            break
