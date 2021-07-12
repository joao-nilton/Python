# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"VALOR DO PRODUTO"\033[m'))
print('=' * 312)  
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

valor = float(input('Qual o valor do produto: '))
print('FORMAS DE PAGAMENTO')
print('\n[1] Pagamento à vista dinheiro/cheque.')
print('\n[2] Pagamento à vista no cartão.')
print('\n[3] Pagamento em até 2X no cartão.')
print('\n[4] Pagamento em 3X ou mais no cartão.\n')

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
    prestacoes = int(input('\nQuantas parcelas? '))
    desconto4 = valor + ((valor * 20)/100)
    prestacoesjuros = desconto4/prestacoes
    print('\nSua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(prestacoes, prestacoesjuros))
    print('\nO valor total a ser pago é de R$ {:.2f}\n:'.format(desconto4))