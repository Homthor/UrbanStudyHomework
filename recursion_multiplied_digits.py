def get_multiplied_digits(number):
    str_number = str(number).replace('0', '1')
    first = int(str_number[0])
    # Если длина строки меньше либо равна 1, возвращаем само число
    if len(str_number) <= 1:
        return int(str_number)

    # Рекурсивный вызов функции для оставшихся цифр
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
