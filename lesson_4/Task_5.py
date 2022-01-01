from functools import reduce

start_list = list(range(100, 1001, 2))
end_list = reduce(lambda x, y: x*y, start_list)

print(start_list)
print(end_list)
