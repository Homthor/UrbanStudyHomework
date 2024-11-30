# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
# в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).
# Предпологаемый вывод [2, 3, 5, 7, 11, 13] [4, 6, 8, 9, 10, 12, 14, 15]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)+1):
    counter = 0
    is_prime = True
    for j in range(1, i):
        if i % j == 0:
            counter += 1
            if counter >= 2:
                is_prime = False
            if is_prime == True:
                primes.append(i)
            if is_prime == False:
                not_primes.append(i)
                primes.remove(i)
                break

print(primes)
print(not_primes)
