print (' ')
print('=' * 40)
print('Programa para analisar nome.')
print('=' * 40)
print (' ')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('=' * 40)

print('OU...')

print('PARABÉNS'if m <= 3 else 'ESTUDE MAIS')