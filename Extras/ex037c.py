# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"CÁLCULO DE DESCONTOS."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""

print('\033[1;30mObserve as opções abaixo.\n')
print('\033[1;31m1 : Converte decimal para binário')
print('\033[1;32m2 : Converte decimal para hexadecimal')
print('\033[1;33m3 : Converte decimal para octal')
print('\033[1;34m4 : Converte binário para decimal')
print('\033[1;35m5 : Converte hexadecimal para decimal')
print('\033[1;36m6 : Converte octal para decimal')
print('\033[1;37m7 : Para colorir\n')


sel = int(input('Selecione a opçao desejada: '))

num1 = input('\nDigite o número que quer converter: ')

if sel == 1:
    num1a = int(num1, 10)
    num1b= (bin(num1a))
    print('\n{} em decimal equivale a {} em binário\n'.format(num1, num1b[2:]))
elif sel == 2:
    num2a = int(num1, 10)
    num2b= (hex(num2a))
    print('\n{} em decimal equivale a {} em hexadecimal\n'.format(num1, num2b[2:]))
elif sel == 3:
    num3a = int(num1, 10)
    num3b= (oct(num3a))
    print('\n{} em decimal equivale a {} em Octal\n'.format(num1, num3b[2:]))
elif sel == 4:
    num4a = int(num1, 2)
    print('O numero {} em binário equivale a {} em decimal '.format (num1, num4a))
elif sel == 5:
    num5a = int(num1, 16)
    print('O numero {} em hexadecimal equivale a {} em decimal '.format (num1, num5a))
elif sel == 6:
    num6a = int(num1, 8)
    print('O numero {} em octal equivale a {} em decimal '.format (num1, num6a))
else:
    print('\nOpçao inválida.\n')


#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))