
print (' ')
print('=' * 40)
print('Programa para analisar o primeiro e último nome de uma pessoa')
print('=' * 40)
print (' ')

nome = str(input( 'Digite um nome:  ')).strip().split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) # [] -> define uma lista em python

print('=' * 40)