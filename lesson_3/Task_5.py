def my_func():
    sum_res = 0
    quit = False
    while quit == False:
        number = input('Введите числа или Q для выхода - ').split()

        res = 0
        for element in range(len(number)):
            if number[element] == 'q' or number[element] == 'Q':
                quit = True
                break
            else:
                res = res + int(number[element])
        sum_res = sum_res + res
        print(f'Тякущяя сумма: {sum_res}')
    print(f'Итоговая сумма: {sum_res}')
my_func()
