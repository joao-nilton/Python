# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))
print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"NÚMEROS PARES"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

#print('Contagem regressiva para queima dos fogos')
#for c in range(0, 51 ): # ou (10, -1, -1) para contar até zero.
for num in range (0, 51, 2):
    print('.', end = '')
    print(num, end=' ')
print('\n ')
print('OU...')
print(' ')
print ('\033[3;33;44mNúmeros pares entre 1 e 50\033[m')
print(' ')
n = 0

for n in range (1, 51): # ocorre maior numero de iteraçoes. para ver print('.', end = '')
    if n % 2 == 0 :
        print(n, end=' ')
print('\n\nFIM\n')


#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))