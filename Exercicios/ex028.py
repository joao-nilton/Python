import random
print (' ')
print('=--=' * 40)
print('JOGO DA ADIVINHAÇÃO')
print('=--=' * 40)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('+--+' * 40)
print (' ')

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
num1 = random.randint(0, 5)

if num != num1:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(num1, num))
else:
    print('PARABÉNS! Você conseguiu me vencer! Eu tambem pensei no número {}'.format(num))
    
print (' ')