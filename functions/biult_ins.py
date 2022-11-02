# Встроенные функции


# lambda
# map()
# filter()
# enumerate()
# zip()
# all(), any()


# Анонимные функции - lambda(Обычные фукнции с одной особенностью, у них нет имен)
# lambda функции могут принимать сколько угодно параметров, но всегда возвращают одно выражение

# def hello(): return 'hello'

# print(hello())

# x = lambda: 'hello'
# print(x())


# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 2))

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2

# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(50))
# print(my_doubler(150))
# print(my_doubler(500))
# print(my_tripler(1000))
# print(my_tripler(4000))

# dict_ = {'John': 500, 'Tirion': 170_000, 'Tom': 150, 'Sanzhar': 20, 'Ayana': 100_000}

# new_dict = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
# print(dict(new_dict))

# ----------------------------------

# map(function, iterable) - применяет к каждому элементу внутри iterable функцию котору мы ей передаем, закидвая в результат те данные которые возвращает функция, в результате мы получаем mapobject(iterator) в котором хранятся все наши данные

# Например, с помощью map можно преобразовать все элементы внутри списка. Перевести все строки в вверхний регистр

# ls = ['one', 'two', 'three', 'four', 'five']

# new_ls = list(map(str.capitalize, ls))
# print(new_ls)

# names = ['John', 'Aikol', 'Aizirek', 'Nurayim', 'Sanzhar']
#     # ['Hello, mr/mrs John', 'Hello, mr/mrs Aikol']


# new_ls = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(new_ls)


# dict_ = {1: 2, 3: 4, 5: 6}
#     # {1: '2', 3: '4', 5: '6'}

# result = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(result)

# -----------------------------------
# filter(function, iterable) -> применяет ко всем элементам iterable фукнцию которую мы переадли и возвращает filterobject(итератор) только с теми элементами, для которых функция вернула True

# ls = ['one', 'two', '3', '', '1', '100', 'John99']

# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['John', 'one', 'two', 'list', 'makers', 'ev.25', 'fanta']
# result = list(filter(lambda x: len(x) > 4, ls))
# print(result)
# -------------------------------------------

# enumerate(iterable) - она пронумеровывает каждый элемент внутри iterable, ее собсвенным индексом 

# ls = ['str1', 'str2', 'str3']

# x = list(enumerate(ls))
# print(x)

# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

# --------------------------------
# zip(iterables) - она соединяет каждый элемент итерируемых элементов между собой, соединяет в тип данных tuple() и возвращает его

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]
# res = list(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10, 20 ,30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей
# x = [(1, 2), (3, 4)]
# dict_ = dict(x)
# print(dict_)

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# d_values = ['castle_r1', 'winterfell', 'Starks', 'Cisco R1', '10.255.101.10']

# res = dict(zip(d_keys, d_values))
# print(res)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'r1': ['london_r1', '21 New Globe Walk', 'Cisco', 'DYR-25', '10.255.101.10'],
#     'r2': ['london_r2', 'Greenwich', 'Cisco', 'Pir-24', '98.255.10.11'],
#     'sw2':  ['london_sw2', 'Mercyside', 'Cisco', '3850', '101.255.20.10'],
# }

# london_data = {}
# for key in data:
#     london_data[key] = dict(zip(d_keys, data[key]))

# print(london_data)

# ---------------------------------------
# all(), any()

# all(iterable) - Возвращает True, если ВСЕ элементы внутри iterable имеют значение True, иначе возвращает False.

# [1,2] -> True
# [] -> False
# 5 -> True
# 0 -> False
# -5 -> True
# 's' -> True
# '' -> False
# ' ' -> True

# ls = [[5,6], '5', 'stroka', True, 1, '']
# print(all(ls))

# ip = '10.255.1y.108'
# ip1 = '10.255.18.108'
# ip2 = '118.20.101.108t'
# result = all(i.isdigit() for i in ip.split('.'))
# result1 = all(i.isdigit() for i in ip1.split('.'))
# result2 = all(i.isdigit() for i in ip2.split('.'))
# print(result)
# print(result1)
# print(result2)

# any - Возвращает True, если хотя бы один из элементов дает True

# ls = [0, 0, [], (), '', [1,2]]
# print(any(ls))


# ignore = ['rm -rf', 'reset', 'chmod']
# command = input('Vvedite commandu: ')

# if any(word in command for word in ignore):
#     raise Exception('Invalid command!')
# else:
#     print('vse ok!')
















