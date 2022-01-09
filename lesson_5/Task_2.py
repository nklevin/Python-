while True:
    with open("task_2.txt", encoding='utf-8') as working_file:
        lines = [line for line in working_file.readlines() if line != '\n']
        print(f"В файле непустых строк:", len(lines))
    for line in lines:
        print(f'Строка {line[:50]}... содержит {len(line.split())} слов')
    break
