number = int(input('Введите число: '))

m = number % 10
a = number // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

