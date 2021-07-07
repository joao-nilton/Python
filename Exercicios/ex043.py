# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"IMC"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

peso = float(input('Digite o seu peso em kilograma: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso/altura**2

if imc < 18.5:
    print('\nVocê está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('\nVocê está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('\nVocê está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('\nVocê está com obesidade. ')
else:
    print('\nVocê está com obesidade mórbida')

'''
IAC significa Índice de Adiposidade Corporal. É um novo método que usa o tamanho dos quadris para medira gordura do corpo
%G = ((Circunferência Quadril (cm))/Altura (m) X srt(altura(m))) - 18

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