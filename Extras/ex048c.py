print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"SOMA DOS MÚLTIPLOS DE 3 ATÉ 500"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

# Este abaixo é o primeiro a dar o valor correspondente ao exercício mas a != mostru-se desnecessária    
sum = 0
for c in range(0, 501, 3):
   if c % 2 != 0 and c % 3 == 0:
    sum += c
    print(c, end=' ')
print('\n\nO somatório de todos os valores foi \033[1;34m{}\033[m'.format(sum))
print(' + - + ' * 20 )
print(' ')

# OU
# Opa deu um resultado interessante abaixo. Foi a soma de todos os numeros pares multiplos de 3

sum = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        sum += c
        print(c, end=' ')

print('\n\nO somatório de todos os valores foi \033[1;34m {}\033[m'.format(sum))
print(' ++ ' * 20 )
print(' ')


# Com contador. Resolução Guanabara
print('--' * 20 )
print(' ')
sum = 0
cont = 0
for c in range(1, 501, 2):

    if c % 3 == 0:
        cont = cont + 1 # ou cont +=1 ( 83 ímapres divisiveis por 3)
        sum += c

print('A soma de tosdos os {} valores solicitados é {}'.format(cont, sum))
print('--' * 20 )
print(' ')

# Este é para ver a tabulação do count

sum = 0
cont = 0
for c in range(1, 501, 2):

    if c % 3 == 0:
        sum += c
    cont = cont + 1 # ou cont +=1 ( 520 ímpares)
print('\033[1;34mA soma de tosdos os {} valores solicitados é {}\033[m'.format(cont, sum))


# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))