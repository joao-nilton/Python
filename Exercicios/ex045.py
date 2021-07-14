# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"PEDRA, PAPEL, TESOURA"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

'''
Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).
Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas.
'''
from random import choice

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4 ]

sorteio = choice(lista)
print (' ')
print('O (A) aluno(a) sorteado foi {}: '.format(sorteio))

from random import randint
from time import sleep
print (' ')
print('=--=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=--=' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('+--+' * 20)
print (' ')

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
#num1 = random.randint(0, 5)
num1 = randint(0, 5)