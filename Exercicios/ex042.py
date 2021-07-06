# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"TRIÂNGULOS"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

print ('Ou...')

lado1 = float(input('Digite o  valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado:  '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 +lado2:
#if lado1 > lado2 - lado3 and lado2 > lado1 - lado3 and lado3 > lado1 - lado2: * não deu certo porque o valor da diferenca é em módulo.
    print('\nOs segmentos acima podem formar um triângulo') 
    if lado1 == lado2 and lado1 == lado3 and lado3 == lado2:
        print('Este triângulo é equilátero')  
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print('Este triângulo é isósceles')  
    elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        print('Este triângulo é escaleno')  
else:
    print('\nOs segmentos acima não podem formar um triângulo')

'''    a = float(input('Primeiro lado: '))
    b = float(input('Segundo  lado: '))
    c = float(input('Terceiro lado: '))
    
    # Testando se é triângulo
    if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
    elif (a == b) and (a == c) :
        print('Equilatero')
    elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
    else:
        print('Escaleno')

      # Este é o programa do Guanabara.
        r1 = float(input('Primeiro segmento: '))
        r2 = float(input('Segundo segmento: '))
        r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
    print(' OS segmentos acima podem formar um triângulo ', end='')
        if = r1 == r2 == r3:
            print('EQUILÁTERO!')
        elif r1 != r2 != r3 != r1:
            print('ESCALENO')
        else:
            print('ISÓSCELES!')
else:
    print('OS segmentos acima NÃO PODEM FORMAR triângulo. ') '''