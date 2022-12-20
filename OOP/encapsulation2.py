# Аннотации свойств (@property(getter, setter))


# class Person:
#     __age = 22

#     @property
#     def age(self):
#         '''The property(getter)'''
#         print('getter')
#         print(type(self.__age))
#         return self.__age

#     @age.setter
#     def age(self, value):
#         '''The age setter'''
#         print('setter')
#         if not isinstance(value, int) or not 0 <= value < 170:
#             raise ValueError('Invalid value for human age!') 
#         self.__age = value

    
# obj = Person()
# print(obj.age)
# print('----')
# obj.age = 18
# print('----')
# print(obj.age)


# ----------------------------
#read and write (radius)

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius
    
#     def _get_radius(self):
#         print('Getter, _get_radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('Setter, _set_radius')
#         if not isinstance(value, (int, float)):
#             raise ValueError('radius must be an int or float object!')
#         self._radius = value
    
#     def _del_radius(self):
#         print('Deleter, _del_radius')
#         question = input('Are you sure to delete raius(yes/no)?')
#         if question.strip().lower() == 'yes':
#             del self._radius
#             print('Deleted!')
#         else:
#             print('Not deleted! Operation denied!')
    
#     radius = property(fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc='The radius protected property')


# circle = Circle(15)
# print(circle.radius)
# circle.radius = 36
# print(circle.radius)
# del circle.radius
# print(circle.radius)

# ------------------------------
# read-only 

# class CoordinateWriteError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
    
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError('x coordinate is read-only field!')

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, value):
#         raise CoordinateWriteError('y coordinate is read-only field!')

# obj = Point(15, -255)
# print(obj.x)  
# print(obj.y)
# obj.x = 36
# obj.y = 100      

# --------------------------------
# write-only
# import hashlib
# import os

# class User:
#     def __init__(self, username, password) -> None:
#         self.username = username
#         self.password = password

#     @property
#     def password(self):
#         raise AttributeError('Password field is write-only! You cant see the password!')
    
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, (str)):
#             raise ValueError('Invalid value for password!')
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt, 100_000)

# john = User('JohnSnow', 'secretkey')  
# print(john.username)
# # print(john.password)
# print(john._hashed_password)
# john.password = 'johnsnow123456'
# print(john._hashed_password)
# # print(john.password)
