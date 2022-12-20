# Множественное наследование - это когда класс наследуется от двух или более классов

# class A:
#     pass

# print(A.mro())
# print(issubclass(A, object))

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing!')

#     def ride(self):
#         print('We\'re riding on the the ground!')

# class Plane:
#     def play_music_at_station(self):
#         print('We started to listen music!')

#     def fly(self):
#         print('We\'re flying!')

# class FutureAuto(Plane, Auto):
#     pass

# obj1 = FutureAuto()
# obj1.ride()
# obj1.fly()
# obj1.play_music_at_station()

# ------------------------
# MRO(Method Resolution Order) - механизм для корректного поиска родительских методов. Был создан для того чтобы решитьь проблему ромба, которая появилась после введиния класса object в пайтон

# class Zero:
#     def say(self):
#         print('Class Zero')

# class First(Zero):
#     def say(self):
#         print('Class First')

# class Second(Zero):
#     def say(self):
#         print('Class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
    
# obj = MyClass()
# obj.say()
# print(MyClass.__mro__)

# ----------------------

# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class MyMRO(type):
#     def mro(cls):
#         return [object, A, cls, B, X, Y]

# class C(A, B, metaclass=MyMRO):
#     pass

# obj1 = C()
# print(C.mro())

# ----------------------------
# Mixins(Миксины, Примеси)
# В каких случиях:
# 1. вы хотите предоставить множество доп фукнций(методов) для класса. 
# 2. вы хотите использовать одну конретную фукнцию во множетсве разных классов

# class Machines:
#     def start_engine(self):
#         print('started engine!')
    
# class MusicPlayerMixin:
#     def play_music(self):
#         print('Music is playing!')

# class Auto(Machines, MusicPlayerMixin):
#     pass

# class Boat(Machines, MusicPlayerMixin):
#     pass

# class WashingMachine(Machines):
#     pass


# obj_auto = Auto()
# obj_boat = Boat()
# obj_wash = WashingMachine()

# obj_auto.start_engine()
# obj_auto.play_music()
# obj_boat.start_engine()
# obj_boat.play_music()
# obj_wash.start_engine()
# obj_wash.play_music()