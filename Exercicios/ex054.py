# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"CÁLCULO MAIOR IDADE."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

from datetime import date

atual = date.today().year
data_atual = date.today()
print(atual)
print(data_atual)

print (' ')
for c in range (0,3):
    name = input('Digite o seu nome: ')
    dataNasc = int(input('Digite o ano em que você nasceu: '))
    dataAtual = int(input('Digite o ano atual: '))
    age = dataAtual - dataNasc

    print (' ')
    if age <= 18:
        label0 = name
    else:
        label1= name  
print (' ')
print (age)
print ('{} São menores de idade'.format(label0))
print ('{} São maiores de idade'.format(label1))
#print ('{} '.format(sel1))

# Só pra gittar em 21-09-21
# Só pra gittar em 22-09-21
# Só pra gittar em 23-09-21
# Só pra gittar em 27-09-21
# Só pra gittar em 28-09-21
# Só pra gittar em 30-09-21
# Só pra gittar em 01-10-21
# Só pra gittar em 02-10-21
# Só pra gittar em 04-10-21
# Só pra gittar em 07-10-21
# Só pra gittar em 08-10-21
# Só pra gittar em 09-10-21
# Só pra gittar em 18-10-21
# 19-10-21 começou a pegar o bicho na UEMG
# 20-10-21 começou a pegar o bicho na UEMG ... procurei ...
# 22-10-21 começou a pegar o bicho na UEMG ... ontem veio a psi ...
# 23-10-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 25-10-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 26-10-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 28-10-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 03-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 04-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 05-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 08-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 09-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 11-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...
# 12-11-21 começou a pegar o bicho na UEMG ... tô quase desistindo...




#ano = eval (input ("Nasceu em que ano? "))
#mes = eval (input ("Nasceu em que mês? "))
#dia = eval (input ("Nasceu em que dia? "))
#ano_atual = eval (input ("Ano atual? "))
#mes_atual = eval (input ("Mês atual? "))
#dia_atual = eval (input ("Dia atual? "))
#dataNasc = datetime.date(ano)
#dataAtual = datetime.date(ano_atual)

#diferença retorna em timedelta
#diferenca = dataAtual - dataNasc
#Cálculos e Resultados
    #rslt = (diferenca.days / 365.25)
#ano_atual-ano

#print(diferenca)

'''
for c in range(0, 18):
    if c < 18:
        print('Você é menor de idade')
else:
    print('Você é maior de idade')        

print('Voce {} tem {} anos e é menor de idade'.format(name, age))

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