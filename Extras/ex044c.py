# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('\033[1;36m=\033[m' * 312)
print ("  {:^150}  ".format('\033[1;31m"VALOR DO PRODUTO."\033[m'))
print('\033[1;36m=\033[m' * 312)  
print (' ')

"""#############################################################################################################"""

'''
valor = float(input('Qual o valor do produto: '))

print('\nDigite (1) um  para dinheiro/cheque.\n')
print('\nDigite (2) dois para cartão à vista.\n')
print('\nDigite (3) para até 2X no cartão.\n')
print('\nDigite (4) para 3X ou mais no cartão.\n')
pagamento = float(input('Qual a forma de Pagamento? '))


if pagamento == 1:
    desconto1 = (valor - ((valor * 10)/100))
    print('\nO valor a ser pago é de R$ {:.2f}\n:'.format(desconto1))
elif pagamento == 2:
    desconto2 = (valor - ((valor * 5)/100))
    print('\nO valor a ser pago é de R$ {:.2f}\n:'.format(desconto2))
elif pagamento == 3:
    desconto3 = valor 
    print('\nO valor a ser pago é de R$ {:.2f}\n:'.format(desconto3))
elif pagamento == 4:
    desconto4 = valor + ((valor * 20)/100)
    print('\nO valor a ser pago é de R$ {:.2f}\n:'.format(desconto4)) ''' 


    # MODELO GUANABARA

print('{:=^40}'.format('LOJAS GUANABARA\n'))
valor = float(input('Qual o valor do produto: '))
print('''FORMAS DE PAGAMENTO
[1] Pagamento à vista dinheiro/cheque.')
[2] Pagamento à vista no cartão.')
[3] Pagamento em até 2X no cartão.')
[4] Pagamento em 3X ou mais no cartão.\n''')

pagamento = float(input('\033[1;44;33mQual a forma de Pagamento? \033[m'))

if pagamento == 1:
    desconto = (valor - ((valor * 10)/100))
   
elif pagamento == 2:
    desconto = (valor - ((valor * 5)/100))

elif pagamento == 3:
    desconto  = valor 
    parcela = valor/2
    print('\033[1;42;33mSua compra será parcelada em 2x de {}, SEM JUROS.\033[m'.format(parcela))
elif pagamento == 4:
    prestacoes = int(input('\n\033[1;45;33mQuantas parcelas? \033[m'))
    desconto = valor + ((valor * 20)/100)
    prestacoesjuros = desconto/prestacoes
    print('\n\033[1;33mSua compra será parcelada em {}x de R$ {:.2f} COM JUROS.\033[m'.format(prestacoes, prestacoesjuros))
else:
    print( '\033[1;33mOPÇÃO INVÁLIDA.\033[m')
print('\n\033[1;33mSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.\n\033[m'.format(valor, desconto))


#print('\n\033[1;33mO valor do desconto é de R$ {:.2f}.\033[m'.format(p), end=' ') 
#print('\033[1;33mVocê terá que pagar R$ {:.2f}\033[m'.format(pg))
# print(n, end=' ')
#print('\033[3;33;44mOlá, Mundo!\033[m')
#n = int(input('\033[1;34m Digite um numero: \033[m'))
#print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format (n, d))
#print('O triplo de \033[1;31m{}\033[m é \033[1;34m{}\033[m'.format (n, t))
#print('A raiz quadrade de \033[1;31m{}\033[m é \033[1;35m{}\033[m'.format (n, s))
#print('Á soma entre {}{}{} e {}{}{} é {}{}{}'.format (cores['mangenta'],n1, cores['limpa'] ,cores['verde'],n2, cores['limpa'],cores['amarelo'],n1+n2, cores['limpa']))