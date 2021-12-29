name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город: ')
email = input('Введите имейл: ')
telephone = input('Введите телефон: ')

def my_func (name, surname, year, city, email, telephone):
     user_info = [str(i) for i in (name, surname, year, city, email, telephone)]
     return ' '.join(user_info)

print(my_func(name, surname, year, city, email, telephone))
