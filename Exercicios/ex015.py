'''print("\n" * 1)
print('=' * 40)
print('Aluguel de carro ') 
print('=' * 40)
print("\n" * 1)

v = int(input('Digite quantos dias vai alugar o carro: '))
d = float(input('Digite o valor da diária: '))
s =  v * d

print('Você deverá pagar R$ {:.2f}  '.format(s))
print("\n" * 1)
print('=' * 40)'''

print("\n" * 1)
print('=' * 40)
print('Aluguel de carro ') 
print('=' * 40)
print("\n" * 1)

v = int(input('Digite quantos dias vai alugar o carro: '))
k = float(input('Digite quantos quilometros o carro rodou: '))
d = float(input('Digite o valor da diária: '))
e = float(input('Digite o valor por quilometro rodado: '))
s =  v * d
ss = k * e
t = s + ss

print('Você deverá pagar R$ {:.2f} por diária mais R$ {:.2f} por Kilometragem. O total será de R$ {:.2f}' .format(s, ss, t))
print("\n" * 1)
print('=' * 40)