# ls = [2, '2', '4', 4, 45, '101']

# res = [x**2 for x in filter(lambda x: type(x) == int, ls)]
# res1 = [x**2 for x in ls if type(x)==int]
# print(res)
# print(res1)
# ---------------------------------

# from random import choices
# from string import ascii_letters as letters, digits
# from itertools import repeat
# from statistics import mean

# q_pass = int(input('Vvedite kol-vo paroley: '))
# symbols = '_$()-'
# result = {
#     f(choices(letters, k=10), choices(digits, k=5), choices(symbols, k=1)) 
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity: {len(result)}')
# lens = [len(x) for x in result]
# print(f'Average len of passwords: {mean(lens)}')






