data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*structure):
    summa = 0

    for element in structure:
        if isinstance(element,int):
            summa += element
        elif isinstance(element, str):
            summa += len(element)
        elif isinstance(element, (tuple,set,list)):
            summa += calculate_structure_sum(*element)
        elif isinstance(element,dict):
            summa += calculate_structure_sum(*element.items())
        elif element is None:
            pass
    return summa


result = calculate_structure_sum(data_structure)

print(result)