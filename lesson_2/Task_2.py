data = input('Введите значение списка:').split()

j = 0
for i in range(int(len(data) / 2)):
    data[j], data[j + 1] = data[j + 1], data[j]
    j += 2

print(data)
