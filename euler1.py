#!/usr/bin/python3

# Числа

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Сумма чисел кратных 3 и 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, 
# то получим 3, 5, 6 и 9. Сумма этих чисел - 23.
# Найдите сумму всех чисел меньше 1000 кратных 3 или 5.
# Примечание: попробуйте записать решение в одну строку при помощи генератора списка
# и встроенной фукнции sum
def multiples():
    listing = []
    for nombre in range(1, 1000):
        if nombre % 3 == 0 or nombre % 5 == 0:
             listing.append(nombre)
             result = sum(listing)
    list_final = []
    list_final.append(result)
    print("Сумма чисел кратных 3 и 5:",list_final[0])

multiples()



# B. Сумма четных чисел ряда Фибоначчи
# Каждый следующий элемент ряда Фибоначчи получается при сложении 
# двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех элементов ряда Фибоначчи, каждый их которых
# является четным числом и не превышает четырех миллионов.
# Подсказка: разбейте задачу на части: сначала получите сам ряд Фибоначчи,
# зачем получите ряд четных элементов.
def fibonacci():
    def fibonacci_gen(max):
        a, b = 1, 2
        while a <= max:
            yield a
            a, b = b, a + b

    return sum(i for i in fibonacci_gen(4000000) if i %2 == 0)
print("сумму всех элементов ряда Фибоначчи, каждый их которых является четным числом и не превышает четырех миллионов",fibonacci())


# С. Самый большой палиндром
# Число-палиндром с обеих сторон (справа и слева) читается одинаково. 
# Самое большое число-палиндром, полученное произведением двух двухзначных чисел – 9009 = 91 * 99.
# Найдите самый большой палиндром, полученный произведением двух трёхзначных чисел.
def palindrome():
    def element_palindrom(element):
        a = str(element)
        return a == a[::-1]
    list_palidrome = []
    for i in range(999, 100, -1):
        for j in range(999, i-1, -1):
            element = i * j
            if element_palindrom(element):
                list_palidrome.append(element)
    return max(list_palidrome)
print("самый большой палиндром, полученный произведением двух трёхзначных чисел",palindrome())


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Сумма чисел кратных 3 и 5')
    test(multiples(), 233168)

    print()
    print('Сумма четных чисел ряда Фибоначчи')
    test(fibonacci(), 4613732)

    print()
    print('Самый большой палиндром')
    test(palindrome(), 906609)

if __name__ == '__main__':
    main()





