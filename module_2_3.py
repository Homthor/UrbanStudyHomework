my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

print(my_list)
list_index = 0

while list_index < len(my_list) + 1:  # + 1 для вывода условия окончания списка
    if list_index == len(my_list):
        print("Список закончен")
        break
    elif my_list[list_index] == 0:
        list_index += 1
    elif my_list[list_index] > 0:
        print(my_list[list_index])
        list_index += 1
    elif my_list[list_index] < 0:
        print("Встречено отрицательное число")
        break
