# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"CONVERSOR DE MEDIDA DE COMPRIMENTO"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""


print('Este é um conversor de medidas de comprimento') 
m = float(input('\nDigite o valor que quer, em metros, da medida que quer converter: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m *1000
inch = m * 39.3701

print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;32m Kilometros(s)\033[m'. format(m, km)) 
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;33m hectômetro(s)\033[m'. format(m, hm)) 
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;34m decâmetro(s)\033[m'. format(m, dam))
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;35m decímetro(s)\033[m'. format(m, dm))  
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;36m centímetro(s)\033[m'. format(m, cm)) 
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;37m milímetro(s)\033[m'. format(m, mm)) 
print('\n {} \033[1;31mmetro(s)\033[m corresponde a {} \033[1;41m polegada(s)\033[m'. format(m, inch))

#+++++

#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))