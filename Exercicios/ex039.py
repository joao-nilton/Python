# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"ALISTAMENTO MILITAR"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""
''' 
ano_atual = (int(input('Digite o ano corrente: ')))
nascimento = (int(input('\nDigite o ano em que você nasceu: ')))
idade = ano_atual - nascimento
menor = 18 - idade
maior = idade - 18
if idade < 18:
    print ('\nVoce está com {} anos e falta(m) {} ano(s) para você ter que se alistar\n'.format(idade, menor))
elif idade >=19:
    print ('\nVoce está com {} anos e se passaram {} anos do prazo de se alistar\n'.format(idade, maior))
else:
   print('\nVocê está com 18 anos, momento exato de se alistar.\n') '''

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = int(input('\nDigite 1 para sexo masculino e 2 para sexo feminino: '))
idade = atual - nasc
print('\nQuem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

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
