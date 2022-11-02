# Oбработка исключений
# Операторы try...except

# Ошибки Erros -> связаны с кодом:
#     SyntaxError
#     IndentationError
#     TabError

# Исключения Exceptions -> связаны с неправильными данными которые передаются в код
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException # прородитель всех исключений

# try:
#     num = int(input('Enter the number: '))
#     print(num)
#     num2 = int(input('Enter the number2: '))
#     print(num2)
#     print(num / num2)
# except:
#     print('неправильные данные!')
# print('очень важная строчка кода!')


# try ... except

# try:
#     <body try>
# except:
    # <body except> сработает только если ошибка в try
# <else:>
    # <body else> сработает если в операторе try нет ошибки
# <finally:>
    # <body finally> сработает в любом случае 

# try:
#     num1 = int(input('Enter the number: '))
# except:
#     print('Invalid values!')
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('Код закончился!')

# ------------------------
# отображение ошибки

# 1. import sys

# list_ = [1,2,3,4,5]
# index = int(input('Vvedite index: '))
# try: 
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e / (error)

# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'Ooops, we catched {e.__class__} error!')
        
# try:
#     num1 = int(input('Vvedite chislo1: '))
#     print(num1 / 0)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели некорректные данные!')

        
# try:
#     num1 = int(input('Vvedite chislo1: '))
#     print(num1 / 0)
# except ValueError:
#     print('Invalid Values')
# except ZeroDivisionError:
#     print('Divide by 0!')


# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('Na nol\' delit\' nel\'zya!')
# except ValueError:
#     print('Invalid symbols!')
# else:
#     print(result)
# finally:
#     print('The end!')

# -----------------------------------
# from string import digits # digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     num1 = input('Vvedite pervoe chislo: ')
#     num2 = input('Vvedite vtoroe chislo: ')
#     try:
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Vy vveli nepravil\'noe chislo!')
#         continue
    
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





















