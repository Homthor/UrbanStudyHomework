# Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих
# модулей. Задача "Счётчик вызовов": Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К
# сожалению, в Python не предусмотрен подсчёт вызовов автоматически. Давайте реализуем данную фишку самостоятельно!
# Вам необходимо написать 3 функции: Функция count_calls подсчитывающая вызовы остальных функций. Функция string_info
# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем
# регистре. Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в
# этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN. Пункты задачи:
# Создать переменную calls = 0 вне функций. Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях. Создать функцию string_info с параметром string и
# реализовать логику работы по описанию. Создать функцию is_contains с двумя параметрами string и list_to_search,
# реализовать логику работы по описанию. Вызвать соответствующие функции string_info и is_contains произвольное
# кол-во раз с произвольными данными. Вывести значение переменной calls на экран(в консоль).

def count_calls():  # счётчик вызова функций
    global counter
    counter += 1

def string_info(string):    # функция выводит информацию по строке в нужном формате
    count_calls()  # вызов счётчика использования функций
    info = (len(string), string.upper(), string.lower())    # создание кортежа с необходимой информацией
    return info

def is_contains(string, list_to_search):    # функция сравнивает есть ли строка в кортеже пренебрегая регистром
    count_calls()   # вызов счётчика использования функций
    flag = False
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            flag = True     # если строка подобна элементу кортежа - поднятие флага
    return flag


string_1 = "Capybara"
string_2 = "Armageddon"
counter = 0

print(string_info(string_1))
print(string_info(string_2))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(counter)
