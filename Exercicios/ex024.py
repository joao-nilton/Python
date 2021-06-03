
print (' ')
print('=' * 40)
print('Programa para saber se o nome da cidade começa com o nome SANTO')
print('=' * 40)
print (' ')

nome = str(input( 'Digite o nome da cidade em que você nasceu: '))

print(nome[:5].upper() == 'SANTO')
print('=' * 40)
#print(nome.upper().count('SANTO')) 
#print('SANTO'in nome)


