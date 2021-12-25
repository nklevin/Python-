string = input('Введите строку: ')
str_list = string.split()

j = 1
for i in str_list:
  print(j, ": " , i[:10])
  j = j + 1
  