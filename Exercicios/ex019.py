'''import random
pessoas = ['jackeline','Marta','Lilia', 'Luciana']
print
Print ('SORETIO')
print
print ('A sorteada foi: ') + pessoas [random.randrange(len(pessoas))]
print '''

'''import random

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4 ]

sorteio = random.choice(lista)
print (' ')
print('O (A) aluno(a) sorteado foi {}: '.format(sorteio))
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