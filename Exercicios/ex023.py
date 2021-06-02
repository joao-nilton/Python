
'''print (' ')
print('=' * 40)
dados = str(input( 'Digite um número de 0 a 9999 com 4 digitos: ')).zfill(4)


print('=' * 40)
print (' ')
print('O numero digitado foi {} '. format(dados))
print (' ')

dividido = dados.split()

print(' O milhar   é {}'.format(dividido[0][3]))
print(' A centena  é {}'.format(dividido[0][2]))
print(' A dezena   é {}'.format(dividido[0][1]))
print(' A unidade  é {}'.format(dividido[0][0]))

'''

num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))

# Esse de cima ainda está com erro. Precisa de estruturaas condicionais. Não é a melhor maneira nesse momento.

'''
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


'''


# Vou colocar um comentário par subir git 28/05/21
# Vou colocar um comentário par subir git 29/05/21
# Vou colocar um comentário par subir git 31/05/21
# Vou colocar um comentário par subir git 01/06/21
