def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()

print_params(2024, False, 'LOZH')

print_params(b = 25)

print_params(c = [1, 2, 3])

values_list = ["ТЕКСТ", 128, 52.42]

values_dict = {'a': 1, 'b': 2, 'c': 3}

values_list_2 = [54.32, 'Aboba']

print_params(*values_list)

print_params(**values_dict)

print_params(*values_list_2, 42)
