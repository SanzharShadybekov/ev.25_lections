# num = 1
# while num >= 0:
#     try:
#         num = int(input('Введите число: '))
#     except ValueError:
#         pass
# else:
#     print('Встретилось отрицательное число!')

# ------------------------------------------

# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(1, 50))

# print(ls)
# ls = list(set(ls))
# res = sorted(ls)
# print(res)

# ----------------------------------

# def introduce(name, last_name, wife='холост', **kwargs):
#     print(f'Привет это {name} {last_name}')
#     print(f'Он {wife}!')
#     if kwargs:
#         print(f'Инициалы его жены {" ".join(kwargs.values())}')

# introduce('John', 'Snow')
# introduce('Tirion', 'Lanister', 'Женат', wife_name='Sansa', wife_last_name='Stark')

# -----------------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor',
# }

# users = [
#     {
#         'id': 1,
#         'username': 'John',
#         'role': roles[0]
#     }, 
#     {
#         'id': 3,
#         'username': 'Tirion',
#         'role': roles[2]
#     },
#     {
#         'id': 2,
#         'username': 'Raychel',
#         'role': roles[1]
#     }
# ]

# product = {
#     'id': 1,
#     'title': 'Iphone 14',
#     'description': 'Lorem Ipsum',
#     'price': 1200
# }
# print(f'Before: {product}')

# id_user = int(input('Vvedite svoi id: '))
# try:
#     user = list(filter(lambda x: x['id'] == id_user, users))[0]
#     print(f'Welcome {user}!')
# except IndexError:
#     raise ValueError('Invalid id for user! User with this id does not exists!')

# if user['role'] == roles[0]:
#     choice = input('Vvedite chto izmenit\': ')
#     product[choice] = input('Vvedite novoe znacheniye: ')
# else:
#     raise Exception('Permission denied!')

# print(f'After: {product}')

# ---------------------------------------

# '''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, возращать финальное количество денег. Мин период вложения 3 года. Мин ставка денек 30 000 сомов'''

# def get_percentage(money, period):
#     if money < 30_000:
#         raise Exception('Min stavka 30000 somov!')
#     if period < 3:
#         raise Exception('Min srok 3 goda!')
    
#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money = money * 1.1
#         # money = money + (money / 100 * 10)
#         i += 1
#     return money
    
# money = int(input('Vvedite summu deneg: '))
# year = int(input('Vvedite srok vashego deposita: '))

# print(get_percentage(money, year))

# ----------------------------
# Дан список внутри которого списки из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,15,5], [5,5,5,5]] -> 6, 23, 20 -> 23

# ls = [[100,2,3], [300,3,5], [200,50,50,50], [45,45,6]]

# def find_max(ls):
#     return max(sum(x) for x in ls)

# print(find_max(ls))

# ---------------------------------
# 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# you! meet to Nice Snow. is name....

# hello john snow king
# king snow john hello

# def get_reverse_string(text):
#     spisok = text.split()[::-1]
#     return ' '.join(spisok)

# print(get_reverse_string('Hello world! My name is John, last name is Snow. Nice to meet you!'))
# print(get_reverse_string('hello john snow king'))







