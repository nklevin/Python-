import random

start_list = []
n = 30
for i in range(n):
    start_list.append(random.randint(0,12))
print(start_list)

unique = list(dict.fromkeys(start_list))
print(unique)
