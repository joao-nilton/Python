print("\n" * 1)
print('=' * 40)
print('Aluguel de carro ') 
print('=' * 40)
print("\n" * 1)

v = int(input('Digite quantos dias vai alugar o carro: '))
d = float(input('Digite o valor da diária: '))
s =  v * d

print('Você deverá pagar R$ {:.2f}  '.format(s))
print("\n" * 1)
print('=' * 40)