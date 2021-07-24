# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"SOMA DOS MÚLTIPLOS DE # ATÉ 500"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

    
sum = 0
for c in range(0, 501, 3):
   # n = int(input('Digite um valor: '))
   if c % 2 != 0 and c % 3 == 0:
    sum += c
    print(c, end=' ')

print('\nO somatório de todos os valores foi {}'.format(sum))

# OU
# Opa deu um resultado interessante abaixo. Foi a soma de todos os numeros pares multiplos de 3
sum = 0
for c in range(0, 501, 2):

   if c % 3 == 0:
    sum += c
    print(c, end=' ')

print('\nO somatório de todos os valores foi {}'.format(sum))





#+++++

# print(n, end=' ')

#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))