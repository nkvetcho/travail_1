#!/usr/bin/python3

# Списки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более, 
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.
def match_ends(words):
    compteur = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            compteur += 1
    return compteur
print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))

# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков
def front_x(words):
    return sorted(words, key=lambda word: (word[0] != 'x', word))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


# C.
#Сортировка по последнему числу
# Дан спискок непустых списков.
# Нужно вернуть список, отсортированный по
# возрастанию последнего элемента каждого подсписка.
# Например: из [[1, 7], [1, 3], [3, 4, 5], [2, 2]] получится
# [[2, 2], [1, 3], [3, 4, 5], [1, 7]]
# Подсказка: используйте параметр key= функции сортировки,
# чтобы получить последний элемент подсписка.

def sort_last(lists):
    return sorted(lists, key=lambda x: (x[-1], x[0]))
ma_liste = [[1, 7], [1, 3], [3, 4, 5], [2, 2]]
print(sort_last(ma_liste))

# D. Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4]. 
def remove_adjacent(nums):
    i=0
    while i < len(nums):
        if nums[i-1]==nums[i]:
            del nums[i]
        i+=1
    return nums
l = [1, 2, 2, 3, 4, 4]

print(remove_adjacent(l))



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
    print('Начало и конец совпадают')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('Начинающиеся с X в начале')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('Сортировка по последнему числу')
    test(sort_last([[1, 3], [3, 2], [2, 1]]),
       [[2, 1], [3, 2], [1, 3]])
    test(sort_last([[2, 3], [1, 2], [3, 1]]),
       [[3, 1], [1, 2], [2, 3]])
    test(sort_last([[1, 7], [1, 6], [3, 4, 5], [2, 2]]),
       [[2, 2], [3, 4, 5], [1, 6], [1, 7]])

    print()
    print('Удаление соседей')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
    test(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
    test(remove_adjacent([]), [])


if __name__ == '__main__':
    main()
