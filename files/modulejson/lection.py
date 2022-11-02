# JSON - JavaScript Object Notation
# Единый формат, хранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть интернет.
# <filename>.json # файл в формате json

# {
#     "id": 1,
#     "author": "Ed Sheeran",
#     "title": "Perfect",
#     "year": 2015,
#     "hit": true
# } --- Это JSON
# наша задача научиться переводить данные JSON в Python Dcitionary

# !!!!!!
# JS object == {key: value}
# PY dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и Десериализации данных

# Сериализация (Запись данных в JSON) - Это перевод из Python в JSON формат

# dump -> метод записывает Python данные в файл в формате JSON, параллельно сделав сериализацию
# dumps - метод записывает Python данные в текст в формате JSON, параллельно сделав сериализацию

# Десериализация (Чтение данных из JSON) - это процесс перевода из JSONa в PY dict

# load - метод который считывает файл в формате JSON и переводит его в PY dict
# loads - метод который считывает текст в формате JSON и переводит его в PY dict


# -----------------------
# процесс сериализации

# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)

# print()
# print(json_text)
# print(type(json_text))

# ----------------------------------
# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print(type(dict_))

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)

# -----------------------------
# Процесс десериализации
# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)

# dict_ = json.loads(json_data)
# print(dict_)
# print(type(dict_))

# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))

# ------------------------------
# https://34.12.121.10/users/ -> запрос на получение

# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)

# # print(json_data)
# # print(type(json_data))

# dict_ = json.load(json_data)
# print(dict_)
# print(type(dict_))
