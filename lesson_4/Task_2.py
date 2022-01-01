from random import  sample

start_list = sample(range(0,300),20)
end_list = [element for i, element in enumerate(start_list) if i > 0 and start_list[i] > start_list[i - 1]]

print(f'Представленный список чисел: {start_list}')
print(f'Полученный список чисел: {end_list}')
