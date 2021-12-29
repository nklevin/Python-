first_argument = int(input('Введите первое число:'))
second_argument = int(input('Введите второй число:'))
third_argument = int(input('Введите третье число:'))

def my_function (first_argument, second_argument, third_argument):
    res_sort = sorted([first_argument, second_argument, third_argument])
    return res_sort[1] + res_sort[2]

print(my_function(first_argument, second_argument, third_argument))
