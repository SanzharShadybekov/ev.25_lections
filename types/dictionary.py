# dict() - Словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered). Каждый элемент в словаря хранится в виде пары: {ключ: значение}

# ассоциативный массив, hash tables, object(js), structure == dictionary(py)

# ключами могут выступать только неизменяемые типы данных и в словаре хранятся уникальные ключи. Тогда как значениями могут высптупать любые типы данных.

# a = 1
# a = 2

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967,
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])

# a = dict()
# b = {}
# c = {1,2}
# print(a, b, c)
# print(type(a))
# print(type(b))
# print(type(c))

# ls = [('key1', 'value1'), ('key2', 'value2')]
# dict_ = dict(ls)
# print(dict_)

# --------------------------
# print(dir(dict))

# items, keys, values

user_info = {
    'first_name': 'John',
    'last_name': 'Snow',
    'age': 24,
    'email': 'johnsnow@gmail.com',
    'role': 'admin',
}

# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
#     print(value)

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')

# ls = list(user_info.items())
# print(ls[0][1])

# изменения элементов в словаря

# dict_ = {'name': 'Jack', 'age': 24}

# print(dict_['name'])
# dict_['name'] = 'John'
# dict_['address'] = 'WinterFell'
# print(dict_)

# dict_.update({'name': 'John', 'address': 'WinterFell'})
# print(dict_)

# -------------------------------

# Создание - fromkeys
# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

# -----------
# get
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.get(2))
# print(dict_[2])

# setdefault - работает так же как и get, но если нет такого ключа, то он создает новую пару из этгго ключа

# dict_ = {'name': 'Eddard', 'last_name': 'Stark',}
# print(dict_)
# print(dict_.setdefault('age', 38))
# print(dict_)

# удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow'}

# removed = dict_.pop('address')
# print(dict_)
# print(removed)

# popitem() - удаляет последнию пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)





