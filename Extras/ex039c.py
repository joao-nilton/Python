# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"ENGAJAMENTO."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""
from datetime import date

atual = date.today().year
nasc = int(input('\033[1;33mAno de nascimento: \033[m'))
sexo = int(input('\n\033[1;32mDigite 1 para sexo masculino e 2 para sexo feminino: \033[m'))
idade = atual - nasc
print('\n\033[1;31mQuem nasceu em {} tem {} anos em {}\033[m'.format(nasc, idade, atual))

if sexo == 1:
    if idade == 18:
        print('\nVoce tem que se alistar IMEDIATAMENTE\n')
   
    elif idade < 18:
        saldo = 18 - idade
        print('\nAinda falta(m) {} anos para o alistamento\n'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em  {}\n'.format(ano))

    elif idade > 18:
        saldo = idade - 18
        print('\nVocê ja deveria ter se alistado ha  {} anos\n'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento deveria ter sido em  {}\n'.format(ano))
elif sexo == 2:
    print('\nO alistamento para o sexo feminino não é obrigatório')

else:
   print('\nMas a opção que você escolheu é inválida')



#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))