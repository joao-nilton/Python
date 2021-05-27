print (' ')
print('=' * 40)
dados = input( 'Digite um número de 0 a 9999: ')

nomed = dados.split()
numdi = len(nomed[0])

print('=' * 40)
print (' ')
print('O numero digitado foi {} e possui {} digitos'. format(dados, numdi))