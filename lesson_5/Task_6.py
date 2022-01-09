output = {}
with open("Task_6.txt", 'r', encoding='utf-8') as working_file:
  for line in working_file:
    values = line.split()
    output.update(
        {
            values[0][0:-1]:
            (int(values[1].split("(")[0]) if values[1] != '—' else 0) + (int(values[2].split("(")[0]) if values[2] != '—' else 0) + (int(values[3].split("(")[0]) if values[3] != '—' else 0)
        }
    )
print(output)