# modulo colorize. ver depois.

print (' ')
print('=--=' * 20)
print('CORES NO TERMINAL')
print('=--=' * 20)

# \033[   Style; text; back m

print('\033[3;33;44mOlá, Mundo!')
a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print (' ')
print('\033[3;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print (' ')

nome = str(input('Digite seu nome: '))
print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format('\033[7;31m', nome, '\033[m'))

nome = str(input('Digite seu nome: '))
cores ={'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[1;30m'}
print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47

