import math

print('=' * 40)
print('Este é um medidor de seno, cosseno e tangente a partir do angulo em graus.') 
print('=' * 40)

an = float(input('Digite o o valor do angulo em graus: '))
x = an * math.pi/180
s = math.sin(x)
c = math.cos(x)
t = math.tan(x)

print('O valor do seno  é {:.3f}'.format(s))
print('O valor do coseno  é {:.3f}'.format(c))
print('O valor da tangente  é {:.3f}'.format(t))
print('=' * 40)

''' degrees = r * 180/pi e radians = degre * pi/180 '''


'''
print('=' * 40)
print('Este é um medidor de seno, cosseno e tangente a partir do angulo em graus.') 
print('=' * 40)

import math

an = float(input('Digite o o valor do angulo em graus: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print('O angulo de {} tem o seno de {}'.format(an, seno))
print('O angulo de {} tem o cossseno de {}'.format(an, cosseno))
print('O angulo de {} tem a tangente de {}'.format(an, tangente))'''

print('=' * 40)
print('Este é um medidor de seno, cosseno e tangente a partir do angulo em graus.') 
print('=' * 40)

from math import radians, sin, cos, tan

an = float(input('Digite o o valor do angulo em graus: '))
seno = sin(math.radians(an))
cosseno = cos(math.radians(an))
tangente = tan(math.radians(an))

print('O angulo de {} tem o seno de {}'.format(an, seno))
print('O angulo de {} tem o cossseno de {}'.format(an, cosseno))
print('O angulo de {} tem a tangente de {}'.format(an, tangente))

print('=' * 40)