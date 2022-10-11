# sentence = input('Vvediyte predlojeniye: ')

# if sentence[-1] == '?':
#     print('Предложение вопроситиельное')
# else:
#     print('Обычное предложение')

# sentence = input('Vvediyte predlojeniye: ')
# print('Предложение вопроситиельное' if sentence[-1] == '?' else 'Обычное предложение') 
# -----------------------------------
# Ternary operator(Тернарный оператор) - конструкция, которая аналогична по своим свойствам и дейтсвию конрукции if/else, ео при этом записывается в одну строчку кода.
# <выражение если в условии True> if <условие> else <вырадение если False>

# number = 18
# res = 'even number' if number % 2 == 0 and  else 'odd number'
# print(res)

# from string import digits

# symbols = digits + '-'
# print(symbols)
# number = input('Vvedite chislo: ')
# is_correct = True
# for i in number: #567 #67i
#     if i not in symbols: #0123456789-
#         is_correct = False

# if is_correct:
#     print('Yes number!')
#     number = int(number)
#     print('Your number:', number)
#     result = number if number >= 0 else -number 
#                                         # -(-56)
#     print(result)
# else: 
#     print('Invalid values!')
# --------------------------------
#  import string #string.digits
# from string import digits # digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     is_correct_number = True
#     num1 = input('Vvedite pervoe chislo: ')
#     if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False

#     for x in num1:
#         if x not in symbols: # i56yu
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number: # 56 # 56y
#         continue

#     num2 = input('Vvedite vtoroe chislo: ')
#     if len(num2) <= 1 and (num2 == '.' or num2 == '-') or not num2:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#     for x in num2:
#         if x not in symbols: # i56yu
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number: # 56 # 56y
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     operator = input('Vvedite operator(+, -, *, /): ')
    
#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {round(num1 - num2, 2)}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите остановить(yes): ')
#     if choice.lower() == 'yes':
#         flag = False
#         print('Пока!')
        