# Принципы ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация
# 7. Ассоциация
# -------------------------------
# Наследование 
# Позволяет принимать родительские методы и атрибуты для дочернего класса

# Родительский класс
# Дочерний класс
# ---------------------------------
# class Animal:
#     def print_info(self):
#         print('I\'m an animal!')

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()
# --------------------------------------

# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'This animal is {self.name} eats {self.meal}!')

# class Lion(Animal):
#     title = 'lion'
#     meal = 'meat'
#     golos = 'aarrrr!'
#     griva = True

    # def say(self):
    #     print(f'This animal is {self.title}: {self.golos}')

#     def print_info(self):
#         print(f'Griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     meal = 'meat'
#     golos = 'bark!'

# class Koala(Animal):
#     name = 'koalo'
#     meal = 'Efkalit'
#     golos = 'rooaarr'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()
# simba.print_info()

# julian.say()
# julian.eat()

# ---------------------------------------
# class Employee:
#     bonus = 1.5

#     def __init__(self, name, last_name, salary):
#         self.name = name + " " + last_name
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
    
#     def give_increase(self):
#         self.salary = self.salary * self.bonus


# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = language


# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if not emps:
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emp(self, employee):
#         self.emps.append(employee)
    
#     def show_emps(self):
#         return [x.get_info() for x in self.emps]


# dev1 = Developer('John', 'Snow', 1000, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1500, 'JS')
# dev4 = Developer('Raychel', 'Cruse', 1000, 'Python')
# man1 = Manager('Ivan', 'Ivanov', 2000)
# man2 = Manager('Dastan', 'Velikiy', 4000, [dev1, dev4])

# man1.add_emp(dev2)
# man1.add_emp(dev3)
# man2.add_emp(dev2)

# print(f'Manager {man1.get_info()}, has {man1.show_emps()} developers.')
# print(f'Manager {man2.get_info()}, has {man2.show_emps()} developers.')

# man2.give_increase()
# dev2.give_increase()

# print(man2.get_info())
# print(dev2.get_info())

# ------------------------------------

# class Person:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def info(self):
#         print(f'My name is {self.name} {self.last_name}, and I\'m {self.age} years old!')

# class Student(Person):
#     def __init__(self, name, last_name, age, univer):
#         super().__init__(name, last_name, age)
#         self.univer = univer
    
#     def info(self):
#         super().info()
#         print(f'I\'m study in {self.univer}!')

# obj = Student('Kyle', 'Walker', 23, 'KGTU')
# obj.info()
# -------------------------

# class Laptop:
#     def __init__(self, brand, model, description, price):
#         self.brand = brand
#         self.model = model
#         self.desc = description
#         self.price = price

#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'description': self.desc, 'price': self.price}

# class MacBook(Laptop):
#     def __init__(self, brand, model, description, price, year, provider):
#         super().__init__(brand, model, description, price)
#         self.year = year
#         self.provider = provider

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['provider'] = self.provider
#         return repr


# class Acer(Laptop):
#     def __init__(self, brand, model, description, price, videocard, display):
#         super().__init__(brand, model, description, price)
#         self.videocard = videocard
#         self.display = display
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] =  self.videocard
#         repr['display'] = self.display
#         return repr

# obj1 = Laptop('Acer', 'M330', '8gb, 512 SSD', 800)
# obj2 = MacBook('Apple', 'Air', '13`, 8gb, 256 ssd', 1000, 2020, 'China')
# obj3 = Acer('Acer', 'Inspire', '16gb, 1tb ssd', 1000, 'gtx geforce nvidia', '15.6 Full RGB')

# print(obj1.get_info())
# print(obj2.get_info())
# print(obj3.get_info())

# ------------------------------
# class Post:
#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []
#         self.id = 0
    
#     #CRUD
#     def create_post(self, title, body, image):
#         self.id += 1 
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'Successfully created!'}
    
#     def list_posts(self):
#         repr = []
#         for post in self.posts:
#             repr.append({'id': post['id'], 'title': post['title'], 'image': post['image']})
#         return {'status': 200, 'msg': repr}

#     def detail_post(self, id):
#         for post in self.posts:
#             if post.get('id') == id:
#                 return {'status': 200, 'msg': post}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def update_post(self, id, **kwargs):
#         for post in self.posts:
#             if post['id'] == id:
#                 post.update(kwargs)
#                 return {'status': 206, 'msg': 'Successfully updated!'}
#         return {'status': 404, 'msg': 'Not found!'}

#     def delete_post(self, id):
#         for post in self.posts:
#             if post['id'] == id:
#                 try:
#                     self.posts.remove(post)
#                     return {'status': 204, 'msg': 'Successfully deleted!'}
#                 except:
#                     return {'status': 500, 'msg': 'Pni svoego backa!'}
#         return {'status': 404, 'msg': 'Not found!'}


# acc1 = Post('JamesKirk')
# print(acc1.create_post('Good news', 'Ya skoro budu otcom!' , 'https://foto.jpg'))
# print(acc1.create_post('na chile', 'na raslabone', 'https://foto123.jpg'))
# print(acc1.create_post('Ya gulyal', 'na ulice bylo prekrasno!', 'https://image.jpg'))

# print(acc1.list_posts())
# print(acc1.detail_post(2))
# print()
# print(acc1.detail_post(3))
# print(acc1.update_post(3, title='My gulyali'))
# print(acc1.detail_post(3))

# print(acc1.delete_post(2))
# print()
# print(acc1.list_posts())

# ---------------------------
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
    
#     def withdraw(self, amount):
#         # if amount > self.balance:
#         #     print('Недопустимая сумма!')
#         #     return
#         self.balance -= amount
#         #self.balance = self.balance - amount
#         print(f'Ваш баланс: {self.balance} сом')
    
#     def deposit(self, amount):
#         # if amount < 0:
#         #     print('Недопустимая сумма!')
#         #     return 
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()

# account.deposit(1000) 
# account.withdraw(500) 

# ---------------------------------------
# Создайте класс MyString, который будет наследоваться от str.

# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop.


# class MyString(str):
#     def __init__(self, value) -> None:
#         self.string = value

#     def append(self, value: str):
#         self.string = self.string + value
    
#     def pop(self):
#         removed = self.string[-1]
#         self.string = self.string[:-1]
#         return removed
    
#     def __str__(self) -> str:
#         return self.string
    

# obj = MyString("String")
# print(obj)
# obj.append('hello')
# print(obj)
# print(obj.pop())
# print(obj)

# ------------------------
# class CustomError(Exception):
#     def __init__(self, error_name) -> None:
#         self.error = error_name
    
#     def __str__(self) -> str:
#         return f'{self.error}'

# def check_letters(str1):
#     if str1.isupper():
#         return f'ВСЕ ОТЛИЧНО! {str1}'
#     else:
#         raise capitals_error

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# print(check_letters("HELLO"))

# ------------------------------
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass
    
#     @abstractmethod
#     def coding(self):
#         pass


# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         print('11111')
#         self.experience = experience
#         self.languages_backend = languages_backend
    
#     def get_info(self):
#         print(f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование')

#     def coding(self, hour):
#         self.count_code_time += hour


# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         print('22222')
#         self.experience = experience
#         self.languages_frontend = languages_frontend
    
#     def get_info(self):
#         print(f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование')

#     def coding(self, hour):
#         self.count_code_time += hour

# class Fullstack(Backend, Frontend):
#     def __init__(self, experience, languages):
#         self.experience = experience
#         self.languages_backend = languages


# obj = Fullstack('Senior', 'Python and JS')
# print(obj.experience)
# print(obj.languages_backend)
# obj.get_info()

# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return self.side**2

# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return int(0.5 * (self.base * self.height))

# class Pyramid(Triangle, Square):
#     def __init__(self, base, height):
#         super().__init__(base, height)

#     def get_volime(self):
#         return int(0.3 * self.base**2 * self.height)


#
#class CreateMixin:
#    def create(self, todo, key):
#        if key in self.todos:
#            return "Задача под таким ключём уже существует"
#        else:
#            self.todos.update({key: todo})
#            return f'Создали задачу {todo}'
#
#
#class DeleteMixin:
#    def delete(self, key):
#        if key in self.todos:
#            deleted = self.todos.pop(key)
#            return f'удалили {deleted} задачу'
#        else:
#            return "Задачи под таким ключем нет"
#
#
#class UpdateMixin:
#    def update(self, key, new_value):
#        if key in self.todos:
#            self.todos[key] = new_value
#            return f'обновили {new_value} задачу'
#        else:
#            return "Задачи под таким ключем нет"
#
#
#class ReadMixin:
#    def read(self):
#        res = dict(sorted(self.todos.items(), key=lambda x: x[0]))
#        # return res
#        return [x for x in res.values()]
#
#
#class Todo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#    def __init__(self):
#        self.todos = {}
#
#    def set_deadline(self, deadline):
#        from datetime import date, datetime
#        dead = datetime.strptime(deadline, "%d/%m/%Y")
#        today = datetime.strptime(date.today().strftime("%d/%m/%Y"), "%d/%m/%Y")
#        res =  (dead - today).days
#        print(f'До дедлайна {res} день')
#        return res
#
#
#a = Todo()
#print(a.create('Сделать таски 7', 7))
#print(a.create('Сделать tests 2', 2))
#print(a.create('Сделать тесты 1', 1))
#print(a.create('Delete tests 5', 5))
#print(a.update(2, 'Make tests 2'))
#print(a.read())
#print(a.delete(1))
#print(a.read())
#a.set_deadline("31/12/2022")



class ExtensionMixin:
    def add_extension(self, extension):
        self.extensions.append(extension)
        return f"Добавлено новое расширение {extension} для игры {self.name}"

    def remove_extension(self, extension):
        try:
            self.extensions.remove(extension)
            return f'{extension} был отключен от {self.name}'
        except:
            return 'Такого расширения нет в списке.'
    

class Game(ExtensionMixin):
    def __init__(self, game_type, name):
        self.type = game_type
        self.name = name
        self.extensions = []

    def get_description(self, str_):
        return self.name + ' это ' + str_
    
    def get_extensions(self):
        if self.extensions:
            return ' '.join(self.extensions)
        return 'Нет подключенных расширений'
