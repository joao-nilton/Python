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
''' 
from random import choice
from time import sleep
#from random import randint


print('''
#[0] PEDRA
#[1] PAPEL
#[2] TESOURA
''')
jogada = int(input('Qual é a sua jogada? '))

if jogada == 0:
    selecao = 'Pedra'
elif jogada == 1:
    selecao = 'Papel'
elif jogada == 2:
    selecao = 'Tesoura'
else:
    print('Opção inválida')

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 40)

lista = ['Pedra', 'Papel', 'Tesoura']
sorteio = choice(lista)

print('O Computador jogou: {}. '.format(sorteio))
print('O Jogador jogou: {}. '.format(selecao))
print('=-' * 40)

if selecao == 'Pedra' and sorteio == 'Pedra':
    print('EMPATE')
elif selecao == 'Pedra' and sorteio == 'Papel':
    print('COMPUTADOR VENCE')
elif selecao == 'Pedra' and sorteio == 'Tesoura':
    print('JOGADOR VENCE')
elif selecao == 'Papel' and sorteio == 'Pedra':
    print('JOGADOR VENCE')
elif selecao == 'Papel' and sorteio == 'Papel':
    print('EMPATE')
elif selecao == 'Papel' and sorteio == 'Tesoura':
    print('COMPUTADOR VENCE')
elif selecao == 'Tesoura' and sorteio == 'Pedra':
    print('COMPUTADOR VENCE')
elif selecao == 'Tesoura' and sorteio == 'Papel':
    print('JOGADOR VENCE')
elif selecao == 'Tesoura' and sorteio == 'Tesoura':
    print('EMPATE')
else:
    print('Erro! Tente novamente.')
#num1 = random.randint(0, 5)
#num1 = randint(0, 5) '''


# VERSÃO GUANABARA

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print( '''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='* 20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='* 20)

if computador == 0: #copmutador jogou PEDRA.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
    

elif computador == 1: # computador jogou PAPEL.
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: # computador jogou TESOURA.
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
