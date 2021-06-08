#import random
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

if num != num1:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(num1, num))
else:
    print('PARABÉNS! Você conseguiu me vencer! Eu tambem pensei no número {}'.format(num))
    
print (' ')