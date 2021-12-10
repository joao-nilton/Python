# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"IMC."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""
peso = float(input('\033[1;;47;31mDigite o seu peso em kilograma: \033[m'))
print(" ")
altura = float(input('\033[1;;47;31mDigite a sua altura em metros: \033[m'))

imc = peso/altura**2

print ('\nSeu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\n\033[1;;41;37mVocê está abaixo do peso ideal.\033[m\n')
elif imc >= 18.5 and imc < 25:
    print('\n\033[1;;42;37mVVocê está no peso ideal.\033[m\n')
elif imc >= 25 and imc < 30:
    print('\n\033[1;;44;37mVocê está com sobrepeso.\033[m\n')
elif imc >= 30 and imc < 40:
    print('\n\033[1;;43;37mVVocê está com obesidade.\033[m\n')
else:
    print('\n\033[1;;44;37mVVocê está com obesidade mórbida.\033[m\n')

'''
IAC significa Índice de Adiposidade Corporal. É um novo método que usa o tamanho dos quadris para medira gordura do corpo
%G = ((Circunferência Quadril (cm))/Altura (m) X sqrt(altura(m))) - 18

    H              M   
 8 a 20         21 a 32     -> Adiposidade normal
 21 a 25        33 a 38     -> Sobrepeso
 > 25           >  38       -> Obesidade


 IMC = Peso (Kg)/ Altura **2 (m)

    IMC
    < 18.5    -> Abaixo do peso
 18.5 a 25    -> Peso ideal
 25 a 30      -> Sobrepeso
 30 a 40      -> Obesidade
    > 40      -> Obesidade Mórbida
'''





#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))