# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"CATEGORIA DO ATLETA."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""

from datetime import date
atual = date.today().year
nasc = int(input('\033[1;36mDigite o ano de nascimento do atleta: \033[m '))
# sexo = int(input('\nDigite 1 para sexo masculino e 2 para sexo feminino: '))
idade = atual - nasc

print('\033[1;31mO atleta tem\033[m\033[1;33m {} \033[manos'.format(idade))



if idade > 1 and idade <= 9:
    print('\n\033[1;32mClassificação:\033[m \033[1;342009mAtleta MIRIM\033[m')
elif idade <=14: 
    print('\n\033[1;32mClassificação:\033[m \033[1;34mAtleta INFANTIL\033[m')
elif idade <= 19:
    print('\n\033[1;32mClassificação:\033[m \033[1;34mAtleta JÚNIOR\033[m')
elif idade <= 25:
    print('\n\033[1;32mClassificação: \033[m\033[1;34mAtleta SÊNIOR\033[m')  
else:
    print('\nClassificação: Atleta MASTER')


#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))