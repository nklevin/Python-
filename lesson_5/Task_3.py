while True:
    with open("task_3.txt", encoding='utf-8') as working_file:
        employees = working_file.readlines()
    for employee in employees:
        name, salary = employee.split()
        salary = int(salary)
        if salary < 20000:
            print('Минимальная зарплата:', name, salary)
    break

summ_salary = 0
summ_salary += salary
print('Средняя зарлата: ', round(summ_salary / len(employees), 2))

