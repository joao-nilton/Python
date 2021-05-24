
import emoji
print(emoji.emojize('Olá Mundo :sunglasses:' ,use_aliases=True))
print(emoji.emojize('Python is :thumbs_up:',use_aliases=True))


# print('\U0001F601')

'''
import random
num1 = random.randint(0, 60 )
num2 = random.randint(0, 60 )
num3 = random.randint(0, 60 )
num4 = random.randint(0, 60 )
num5 = random.randint(0, 60 )
num6 = random.randint(0, 60 )

print(num1, num2, num3, num4, num5, num6)
'''

'''

import random
num = random.random() # por padrão gera um número entre 0 e 1.
num1 = random.randint(1, 10)
print(num)
print(num1)

'''


'''from math import sqrt, floor 

num = float(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrade de {} é {} '.format(num, raiz, ))
print('A raiz quadrade de {} é {:.2f} '.format(num, raiz ))'''






'''
import math
num = float(input('Digite um número: '))
raiz = math.sqrt(num)
# cos = math.cos(num)
# p = math.pow(num)

print('A raiz quadrade de {} é {} '.format(num, raiz, ))
print('A raiz quadrade de {} é {:.2f} '.format(num, raiz ))
print('A raiz quadrade de {} é {} '.format(num, math.ceil(raiz) ))
print('A raiz quadrade de {} é {} '.format(num, math.floor(raiz) ))'''
