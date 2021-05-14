print("\n" * 1)
print('=' * 40)
print('Cálculo de reajuste salarial') 
print('=' * 40)
print("\n" * 1)

v = float(input('Digite o valor do salário atual em Reais: '))
d = float(input('Digite o valor do reajuste salarial em porcentagem: '))
p =  (v * d) / 100
pg = v + p  # ou novo preco = v - (v * d / 100) --> que substituiria as variáveis p e pg


print('O valor corrigido do salário e de R$ {:.2f}'.format(pg))
print("\n" * 1)
print('=' * 40)