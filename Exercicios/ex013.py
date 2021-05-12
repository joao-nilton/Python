print("\n" * 1)
print('=' * 40)
print('Cálculo de reajuste salarial') 
print('=' * 40)
print("\n" * 1)

v = float(input('Digite o valor do salário atual em Reais: '))
d = float(input('Digite o valor do reajuste salarial em porcentagem: '))
p =  (v * d) / 100
pg = v + p

print('O valor corrigido do salário e de  {} Real(is)'.format(pg))
print("\n" * 1)
print('=' * 40)