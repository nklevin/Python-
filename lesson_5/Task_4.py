data = [ 'Ноль','Один', 'Два', 'Три', 'Четыре']

rus = open('task_4_rus.txt', 'w')
with open('task_4.txt', 'r') as working_file:
  for line in working_file:
      s = line.split(' ')
      rus.write(data[int(s[2])] + ' - ' + s[2])
rus.close()
