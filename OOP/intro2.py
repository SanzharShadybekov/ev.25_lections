# class Student:
#     univer = 'MIT'

#     def __init__(self, first_name, last_name):
#         self.name = first_name + ' ' + last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_point(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             self.is_ready_to_work = True
#             print(f'{self.name} is ready to work!')

#     def read_book(self, book):
#         self.add_point(50)
#         self.books.append(book)

#     def do_lab_works(self):
#         self.add_point(50)
    
#     def do_real_project(self):
#         self.add_point(100)
    
#     def learn_new_language(self, language, score):
#         if score in range(60, 101):
#             self.add_point(100)
#             self.languages.update({language: score})
#             # self.languages[language] = score
#         else:
#             raise Exception('Invalid score for language!')

# st1 = Student('James', 'Kirk')
# st2 = Student('Raychel', 'Monella')
# print(st1.name, st1.univer)
# print(st2.name, st2.univer)

# print(f'Before study {st1.name}: \nBooks: {st1.books} \nLanguages: {st1.languages}\nKnowledge: {st1.knowledge}, {st1.is_ready_to_work}.')

# st1.read_book('Martin Iden')
# st1.read_book('Eugene Onegin')

# st1.learn_new_language('Python', 100)
# st1.do_lab_works()
# st1.do_real_project()
# st1.learn_new_language('JS', 80)
# st1.do_real_project()

# print(f'After study {st1.name}: \nBooks: {st1.books} \nLanguages: {st1.languages}\nKnowledge: {st1.knowledge}, {st1.is_ready_to_work}.')

# --------------------------------------------

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def __str__(self):
#         return f'{self.brand} {self.model}'
    
# a = Car('BMW', '7 series')
# print(a)
# b = Car('Mercedez-Benz', 'w140')
# print(b)

# -----------------------------------------

# class Soda:
#     def __init__(self, ingredient: str=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else: 
#             self.ingredient = None
        
#     def print_my_drink(self):
#         if self.ingredient:
#             print(f'Gazirovka so vkusom {self.ingredient}')
#         else:
#             print('The normal gazirovka')

# drink1 = Soda('Grusha')
# drink1.print_my_drink()

# drink2 = Soda()
# drink2.print_my_drink()

# drink3 = Soda(5)
# drink3.print_my_drink()
# ---------------------------

# [5, 6, 7] - True [1,2,6]-False
# class TriangleChecker:
#     def __init__(self, sides: list) -> None:
#         self.sides = sides
    
#     def __str__(self) -> str:
#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return 'Нельзя построить треугольник! Так как все стороны должны быть числами!'
#         if any(x <= 0 for x in self.sides):
#             return 'Нельзя построить треугольник! Так как все стороны должны быть больше нуля!'
#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return 'Нельзя построить треугольник! Так как все сумма двух сторон меньше самой длинной стороны!'
#         return 'Мы можем построить треугольник!'

# t1 = TriangleChecker([19, 6, 8])
# print(t1)
# print(TriangleChecker([5, 6, 7]))
# print(TriangleChecker([5, 6, '7']))
# print(TriangleChecker([5, 6, -1]))
# print(TriangleChecker([3, 2, 4]))


