my_list = [9, 7, 5, 3, 1]
new = int(input("Введите число: "))

while True:
    for part in range(len(my_list)):
        if my_list[part] == new:
            my_list.insert(part + 1, new)
            break
        elif my_list[0] < new:
            my_list.insert(0, new)
        elif my_list[-1] > new:
            my_list.append(new)
        elif my_list[part] > new and my_list[part + 1] < new:
            my_list.insert(part + 1, new)
    print(f"текущий список - {my_list}")
    break
