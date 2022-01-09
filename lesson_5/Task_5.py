import random

output = open("task_5.txt", 'w')
for _ in range(0, 10):
  output.write(str(random.randrange(1000)) + ' ')
output.close()

working_file = open("task_5.txt", 'r')
map_object = map(int, working_file.read().split())
mapping = list(map_object)
working_file.close()

print(sum(mapping))
