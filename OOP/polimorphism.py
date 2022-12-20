# фукнция полиморфизм -> len() : __len__

# print(len('Makers'))
# print(len([1, 2, 'str', 4, 5]))
# print(len({1: '1', 2: '2'}))

# + (__add__) - метод полиморфизм
# print(5 + 5)
# print('hello' + 'Hello')
# print([1,2,3] + [4,5,6])

# Полиморфизм - способность функции(метода) использоваться для разных типов(классов).
# Широко распрастраненное определение: "Один интерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop


# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')
    
#     def make_sound(self):
#         print('Meow, meow!')

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}')
    
#     def make_sound(self):
#         print('Bark bark!')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 7)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()


# from math import pi

# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return f'Я фигура в двумерной плоскости: {self.name}'


# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.length = length 

#     def area(self):
#         return self.length ** 2

#     # def fact(self):
#     #     return 'У квадрата все стороны равны и все углы равны 90 градусам!'

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius
    
#     def area(self):
#         return pi * (self.radius ** 2)
    
# a = Square(6)
# b = Circle(4)

# print(a.fact())
# print(b.fact())

# print(a.area())
# print(b.area())


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.


# class Phone:
#     def __init__(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery_level = 100

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен!')
#         print(f'Уровень заряда: {self.__battery_level}!')
#         self.__battery_level -= 0.5
    
#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен!')
#         print(f'OS: {self.__os}, IMEI: {self.__imei}!')
#         self.__battery_level -= 0.5

#     def play_music(self):
#         if self.__battery_level < 5:
#             raise Exception('Телефон разряжен!')
#         print('Слушаем Мирбека Атабекова!')
#         self.__battery_level -= 5
    
#     def play_video(self):
#         if self.__battery_level <= 10:
#             raise Exception('Недопустимый уровень заряда!')
#         print('Смотрим видосы Кани на платформе!')
#         self.__battery_level -= 7
    
#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             # print(now().strftime('%M:%S'), end_time)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             print(f'Идет зарядка батареи! Ваш уровень батареи: {self.__battery_level}')


# phone = Phone('123 12313 123', 'iOS 15')
# phone.battery_level
# phone.battery_level
# phone.get_info
# phone.battery_level
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(15)
# phone.battery_level
