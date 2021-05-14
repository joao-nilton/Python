print("\n" * 1)
print('=' * 40)
print('Cálculo de descontos') 
print('=' * 40)
print("\n" * 1)

v = float(input('Digite o valor da compra em Reais: '))
d = float(input('Digite o valor do desconto em porcentagem: '))
p =  (v * d) / 100
pg = v - p # ou novo preco = v - (v * d / 100) --> que substituiria as variáveis p e pg

print('O valor do desconto é de R$ {:.2f}.'.format(p), end=' ') 
print('Você terá que pagar R$ {:.2f}'.format(pg))
print("\n" * 1)
print('=' * 40)