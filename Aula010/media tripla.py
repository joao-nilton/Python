print (' ')
print('=' * 40)
print('Programa para analisar nome.')
print('=' * 40)
print (' ')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n1) / 3
print('A sua média foi {:.1f}'.format(m))
if m < 6.0:
    print('Sua média foi ruim! ESTUDE MAIS!')
elif m < 9.0:
    print('sua média foi boa! PARABÉNS!')
elif m > 9.0:
    print('sua média foi boa! ÓTIMO!')
else:
    print('fora da média')
        

    
print('=' * 40)

print('OU...')



