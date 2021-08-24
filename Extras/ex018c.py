# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"CÁLCULO DE DESCONTOS."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""
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

print('\033[1;32mO angulo de\033[m   \033[1;34m{}\033[m    \033[1;32mtem o seno de\033[m     \033[1;34m{}\033[m'.format(an, seno))
print('\033[1;32mO angulo de\033[m   \033[1;34m{}\033[m    \033[1;32mtem o cossseno de\033[m \033[1;34m{}\033[m'.format(an, cosseno))
print('\033[1;32mO angulo de\033[m   \033[1;34m{}\033[m    \033[1;32mtem a tangente de\033[m \033[1;34m{}\033[m'.format(an, tangente))

print('=' * 40)
print('=' * 40)


#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))