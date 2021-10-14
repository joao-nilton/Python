# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"PASSAGEM RODOVIÁRIA"\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""

print (' ')
print('\033[1;33m=--=\033[m' * 20)
print('\033[1;36mPREÇO DA PASSAGEM RODOVIÁRIA\033[m')
print('\033[1;33m=--=\033[m' * 20)

'''num = float(input('Qual a distância de sua viagem? '))


if num <= 200:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num1 = num * 0.50
    print('E o preço da passagem é de {} Reais'.format(num1))
else:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num2 = num * 0.45
    print('E o preço da passagem é de {} Reais'.format(num2))'''

print('OU...')

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a iniciar uma viagem de {}Km'.format(distancia))
preco = distancia * .50 if distancia <= 200 else distancia * .45
print('E o preço de sua passagem sera de R$ \033[1;34m{:.2f}\033[m'.format(preco))

print (' ')



#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))