print (' ')
print('=--=' * 20)
print('AUMENTO SALARIAL')
print('=--=' * 20)

sal = float(input('Digite o valor atual de seu salário: '))
print (' ')
if sal > 1250:
    sal1 = sal + (sal * 10)/100
    print('O seu novo salário será de R$ {}'.format(sal1))

else:
    sal <= 1250
    sal2 = sal + (sal * 15)/100
    print('O seu novo salário será de R$ {}'.format(sal2))