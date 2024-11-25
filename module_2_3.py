mass = (42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5)

print(mass)

for i in range(len(mass)):
    if mass[i] == 0:
        i += 1
    elif mass[i] > 0:
        print(mass[i])
        i += 1
        if i == len(mass):
            print("Список закончился")
    else:
        print("Встречено отрицательное число")
        break
