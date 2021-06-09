print (' ')
print('=--=' * 20)
print('PAR OU IMPAR')
print('=--=' * 20)

num = float(input('Me diga um número qualquer: '))
num1 = num % 2 

if num1 == 0:
    print('O número {} é PAR '.format(num))
else:
    print('O número {} é IMPAR '.format(num))
    
print (' ')
