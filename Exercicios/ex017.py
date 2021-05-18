'''
print('=' * 40)
print('Este é um medidor da hipotenusa a partir da medida dos catetos.') 
print('=' * 40)

co = float(input('Digite o comprimento do cateto oposto em cm: '))
ca = float(input('Digite o comprimento do cateto adjacente em cm: '))
hip = (co**2 + ca**2)** (1/2) 

print('O valor da hipotenusa  é {}'.format(hip))
print('=' * 40)'''

 # import math
 
from math import hypot

print('=' * 40)
print('Este é um medidor da hipotenusa a partir da medida dos catetos.') 
print('=' * 40)

co = float(input('Digite o comprimento do cateto oposto em cm: '))
ca = float(input('Digite o comprimento do cateto adjacente em cm: '))
# hip = (co**2 + ca**2)** (1/2) 
 #hip = math.hypot(co, ca)
hip = hypot(co, ca)

print('O valor da hipotenusa  é {}'.format(hip))
print('=' * 40)