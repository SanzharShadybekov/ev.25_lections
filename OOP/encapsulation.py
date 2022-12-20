# Инкапсуляция:
# 1. Связь данных с методаи которые должны управлять этими данными
# 2. Механизм при помощи которого можно ограничить доступ одних компонентов программы к другим компонентам (сокрытие данных)

# Инкапсуляция как связь

# class Phone:
#     number = '+996 503-503-503'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как управление доступом
# 3 уровня доступа в питоне:
    # 1. Публичный(public) = self.number, def get
    # 2. Защищенный(_protected, parent/child) = _number, def _get
    # 3. Приватный (__private, частный, используются только в текущем классе) = __number, def __get

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.brand = 'BMW' #public
#         self._model = '7 series' #protected
#         self.__motor = 'ABC' #private

#     def _get_date(self):
#         print('1 September')

# class Audi(Car):
#     pass

# class Auto(Audi):
#     pass

# obj = Auto()
# print(obj._country)

# audi = Audi()
# print(audi.brand)
# print(audi._model)
# print(audi._Car__motor)


# car = Car()
# print(car.brand)
# print(car._country)
# print(car._model)
# print(car._Car__motor)
# car._get_date()


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_talks = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('Cбросить или взять: yes/no: ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку')

#     def __turn_on(self):
#         self.__count_of_talks += 1
#         print('Alo!')
#         print(f'Count of talks with Jamie {self.__count_of_talks}')
    
# john = Phone()
# # john.call()
# # john.call()
# john.__turn_on()

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')

# obj = Person('James', 18)
# obj.display_info()
# obj.name = 'Raychel'
# obj.age = -18
# obj.display_info()


# getter & setter
# Они используются для получения и уставки значений, чтобы добавить логику валидации(проверки) данных которые будут установлены в аттрибуты которые имеют защиту
# Еще для того чтобы избежать прямого обращения к защищенному полю класса

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age
    
#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} years old!')
    
#     #getter
#     def get_name(self): 
#         return self.__name

#     #setter
#     def set_name(self, value):
#         if not isinstance(value, str):
#             raise ValueError('Name must be str object!')
#         self.__name = value
    
#     def get_age(self):
#         return self.__age

#     def set_age(self, value):
#         if not isinstance(value, int) or not 0 <= value < 150:
#             raise Exception('Invalid value for age!')
#         self.__age = value

# obj = Person('John', 18)
# print(obj.get_age())
# obj.display_info()
# obj.set_age(25)
# obj.display_info()

# class Kyrgyzstan:
#     __name = 'Kyrgyz Republic'
#     __population = 0

#     def get_population(self): 
#         return self.__population
    
#     def set_population(self, number):
#         if not isinstance(number, int) or number < 0:
#             raise ValueError('The given value is not valid!')
#         self.__population = number
    
#     def display_population(self):
#         print(f'Population of {self.__name}: {self.get_population()}')

# obj = Kyrgyzstan()
# obj.set_population(7_000_000)
# obj.display_population()

