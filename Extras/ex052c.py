# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"NÚMEROS PRIMOS."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""


numero = int(input('\033[1;33mDigite o numero: \033[m '))
#razao = int(input('\033[1;33mRazão:  \033[m '))
#decimo = primeiro + (10 - 1) * razao
print(' ')
for c in range (1, numero + 1):
   # print('{}'.format(c), end=' ')
    if numero%c == 0:
        p = c
        print('\033[1;31m{}\033[m'.format(p), end =' ')

     # Nào estou conseguindo formatar. Hj tem eletromag. Vou só Gitar   
     # Nào estou conseguindo formatar. Hj tem filosofia Vou só Gitar   30/08/21
     # Formatei em 01-09-21
    else:
        numero%c == 1
        p1 = c
        print(p1, end = ' ')
print('\n\n\033[1;41mOs números em vermelho são divisores do número digitado e se houver apens dois o número é primo.\033[m')
print(' ')
print(' ')

# VERSÃO GUANABARA

num = int(input('\033[1;33mDigite um numero: \033[m '))
tot = 0
print(' ')
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')    
    print('{}'.format(c), end=' ')
print(' ')
print(' ')
print('\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!!!')
else:
    print('E por isso ele NÃO É PRIMO!!!')



print(' ')

#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))