# Ou seja, a é o primeiro termo, a + r o segundo, e a + 2r o terceiro.

# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;34m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"PROGRESSÃO ARITMÉTICA - PA."\033[m'))
print('\033[1;34m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""
a = int(input('\033[1;33mQual o valor do primeiro Termo?\033[m '))
r = int(input('\033[1;33mQual é a Razão? \033[m '))
n = int(input('\033[1;33mQual é a quantidade de termos? \033[m '))
print(' ')
an = a + (n - 1) * r
for c in range (a, an + r, r):
    print (c, end='  ->  ')
print(' ')


# print('O primeiro termo é {}, a razão é {} e o último termo vale {}'.format(a,r, ))


#+++++

# print(n, end=' ')

#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))