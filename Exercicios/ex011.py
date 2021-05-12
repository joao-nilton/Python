print("\n" * 1)
print('=' * 40)
print('Cálculo de quantidade de tinta necessária') 
print('=' * 40)
print("\n" * 1)

h = float(input('Digite a altura da parede em metros: '))
b = float(input('Digite a largura da parede em metros: '))
r =  h * b
a = r / 2

print('A área a ser pintada corresponde a {} metro(s)quadrado(s).'.format(r), end=' ') 
print('E serão necessários {} litro(s) de tinta'.format(a))
print("\n" * 1)
print('=' * 40)