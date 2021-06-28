# style --> 0 ,1 , 4, 7     0 = none    1 = bold    4 = underline       7 = negativo    3 = itálico
# text --> 30 = branco      31 = vermelho   32 = verde  33 = amarelo    34 = azul   35 = vmagenta    36 = ciano 37 = cinza
# back (background) mesma do text mas de 40 a 47
# print('{} Muito prazer em te conhecer! {} SSS '.format(cores['pretoebranco'], cores['limpa']))
#print('Olá! Muito prazer em te conhecer {} {} {}!!!,'.format(cores['pretoebranco'], nome, cores['limpa']))

cores ={'limpa':'\033[m', 'branco':'\033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m', 'mangenta':'\033[35m','ciano':'\033[36m','cinza':'\033[37m', 'pretoebranco':'\033[1;30m'}
bkg ={'limpa':'\033[m', 'branco':'\033[40m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m', 'mangenta':'\033[45m','ciano':'\033[46m','cinza':'\033[47m', 'pretoebranco':'\033[1;40m'}

print (' ')
print('=' * 312)
print ("  {:^150}  ".format('\033[1;31m"CONVERSOR DE BASES NUMÉRICAS"\033[m'))
print('=' * 312)  
print (' ')

"""#############################################################################################################"""

print('Observe as opções abaixo.\n')
print('1 : Converte decimal para binário')
print('2 : Converte decimal para hexadecimal')
print('3 : Converte decimal para octal')
print('4 : Converte binário para decimal')
print('5 : Converte hexadecimal para decimal')
print('6 : Converte octal para decimal\n')

sel = int(input('Selecione a opçao desejada: '))

num1 = input('\nDigite o número que quer converter: ')

if sel == 1:
    num1a = int(num1, 10)
    num1b= (bin(num1a))
    print('\n{} em decimal equivale a {} em binário\n'.format(num1, num1b[2:]))
elif sel == 2:
    num2a = int(num1, 10)
    num2b= (hex(num2a))
    print('\n{} em decimal equivale a {} em hexadecimal\n'.format(num1, num2b[2:]))
elif sel == 3:
    num3a = int(num1, 10)
    num3b= (oct(num3a))
    print('\n{} em decimal equivale a {} em Octal\n'.format(num1, num3b[2:]))
elif sel == 4:
    num4a = int(num1, 2)
    num4b= (int(num4a))
    print('\n{} em binário equivale a {} em decimal\n'.format(num1, num4b[2:]))
elif sel == 5:
    num5a = int(num1, 16)
    num5b= (int(num5a))
    print('\n{} em hexadecimal equivale a {} em decimal\n'.format(num1, num5b[2:]))
elif sel == 6:
    num6a = int(num1, 8)
    num6b= (int(num6a))
    print('\n{} em octal equivale a {} em decimal\n'.format(num1, num6b[2:]))
else:
    print('\nOpçao inválida.\n')




'''
https://ichi.pro/pt/binario-hexadecimal-e-octal-em-python-35331013922529

>>> num1 = "0b100"
>>> num2 = "0b110"
>>> mysum = int(num1, 2) + int(num2, 2)
>>> print(bin(mysum))
0b1010

>>> num1 = 0b100
>>> num2 = 0b110
>>> mysum = num1 + num2
>>> print(bin(mysum))
>>> num1 = "0b100"
>>> print(num1)
"0b100"
>>> num1 = 0b100
>>> print(num1)
4
>>> print(bin(num1))
0b100

--------------------

>>> hnum1 = "0x10"
>>> hnum2 = "0x10"
>>> myhsum = int(hnum1, 16) + int(hnum2, 16)
>>> print(hnum1)
"0x10"
>>> print(myhsum)
32
>>> print(hex(myhsum))
0x20
>>> hnum1 = 0x10
>>> hnum2 = 0x10
>>> myhsum = hnum1 + hnum2
>>> print(hnum1)
16
>>> print(myhsum))
32
>>> print(hex(myhsum))
0x20

----------------------------

Os oito dígitos de octal são 0, 1, 2, 3, 4, 5, 6, 7.

Vamos usar o mesmo exemplo de código aqui, mas usaremos a notação adequada e a função de conversão para octal.

>>> onum1 = "0o10"
>>> onum2 = "0o10"
>>> myosum = int(onum1, 8) + int(onum2, 8)
>>> print(onum1)
"0o10"
>>> print(myosum)
16
>>> print(oct(myosum))
0o20
>>> onum1 = 0o10
>>> onum2 = 0o10
>>> myosum = onum1 + onum2
>>> print(onum1)
8
>>> print(myosum))
16
>>> print(oct(myosum))
0o20

--------------------------

A grande vantagem do Python é que ele pode fazer quase tudo, exceto minha roupa. E estou trabalhando nisso.

As lições são simples:

O binário usa bin () e '0b'.
Hexadecimal usa hex () e '0x'.
Octal usa oct () e '0o'.
A função int () pode ser usada para converter números em um inteiro de base 10 de qualquer base entre 2 e 36, alterando o segundo parâmetro. por exemplo, int (número, 30)
'''