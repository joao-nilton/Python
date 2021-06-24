# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"EMPRÉSTIMO BANCÁRIO"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""


valor = float(input('\033[31mQual é o valor do imóvel ?  \033[m'))
sal = float(input('\033[31mQual é o valor do seu salário ?  \033[m'))
amort = int(input('\033[31mEm quantos meses vai pagar ?  \033[m'))
prest = valor/amort
porc = sal * 30/100

print('Para pagar uma casa no valor de R${} em {} meses a prestação será de R${}'.format(valor, amort, prest))
if prest >= (sal * 30/100):
    print('\033[33mNão é possível realizar  o financiamento \033[m')
else:
    print('\033[33mo financiamento será efetivado\033[m')


