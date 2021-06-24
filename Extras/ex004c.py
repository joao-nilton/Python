# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"VERIFICANDO O TIPO"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

n = (input('Digite algo:'))
print('\033[31m''O tipo primitivo desse valor é {}\033[m'.format ( type(n)))
print('\033[32m''É alfabetico: {}\033[m'.format(n.isalpha()))
print('\033[33m''Só tem espaços: {}\033[m'.format (n.isspace()))
print('\033[34m''É um numero: {}\033[m'.format(n.isnumeric()))
print('\033[35m''É alfanumerico: {}\033[m'.format(n.isalnum()))
print('\033[36m''Está em maiúscula: {}\033[m'.format(n.isupper()))
print('\033[37m''Está em minúscula: {}\033[m'.format(n.islower()))
print('\033[47;30m''É printável: {}\033[m'.format(n.isprintable()))
print('\033[1;40m''Está em capitalizada: {}\033[m'.format(n.istitle()))

# Este comentário é do dia 16 de março de 2021
# Este comentário é do dia 17 de março de 2021
# Este comentário é do dia 26 de março de 2021
# Este comentário é do dia 29 de Abril de 2021 - Retorno do Jedi