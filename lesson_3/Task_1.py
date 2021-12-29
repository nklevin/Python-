def my_function(*args):

    try:
        first_number = int(input("Введите число: "))
        second_number = int(input("Введите число: "))
        function_result = first_number / second_number
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return function_result

print(f'Результат:  {my_function()}')
