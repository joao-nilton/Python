
print (' ')
print('=' * 40)
print('Programa para analisar nome')
print('=' * 40)
print (' ')

nome = str(input( 'Digite o seu nome completo: ')).strip()

print('Seu nome tem silva? {}'.format('SILVA' in nome.upper())) # in é operador e não método

print('=' * 40)
