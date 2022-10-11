# /// TASK3 \\\
# Запросите у пользователей 5 раз их имя и фамилию, но в списке сохраните лишь фамилию, также учтите, что
# у человека ФИО может состоять не только из 2 слов. При выводе должен выходить отсортированный
# в алфавитном порядке список

# Наример:
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias Wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff']

# names = ['Maya Angelou', 'Chimamanda Ngozi Adichie', 'Tobias Wolff', 'Sherman Alexie', 'Jane Austen']
# names = []
# for x in range(0, 5):
#     name = input('Vvedite FIO: ')
#     names.append(name)

# result = []
# for x in names:
#     x = x.split(' ')
#     print(x)
#     result.append(x[-1])

# result.sort()
# print(result)

# --------------------------
# range(start, stop, [step]) - возвращает последовательность из целых чисел, начиная с start до stop, возвращает итерируемый тип данных range

# x = range(1, 101)
# print(list(x))
# print(x)
# for num in x:
#     print(num)
# res = 0
# for num  in range(1, 101):
#     res += num

# print(res)

# /// TASK8 \\\
# Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
# Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Результат:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
# list1 = []
# list2 = []
# list3 = []
# for x in range(0, len(list_), n):
#     list1.append(list_[x])
#     list2.append(list_[x+1])
#     if x + 2 >= len(list_):
#         continue
#     list3.append(list_[x+2])

# res = [list1, list2, list3]
# print([['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])
# print(res)

# /// TASK5 \\\
# Создайте список с 3 вложенными списками , где внутри должно быть три 0
# Результат:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# res = []
# for x in range(0, 3):
#     ls = []
#     for x in range(0, 3):
#         ls.append(0)
#     res.append(ls)

# print(res)

# /// TASK4 \\\
# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# list_ = [1, 2, 3]
# Результат:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# from itertools import permutations

# res = list(permutations([1, 2, 3], 3))
# print(res)













