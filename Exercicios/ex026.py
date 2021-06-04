
print (' ')
print('=' * 40)
print('Programa para analisar letra A')
print('=' * 40)
print (' ')

nome = str(input( 'Digite uma frase:  ')).strip()

print('A letra A aparece {} vezes na frase'.format(nome.upper().count('A')))
print('A primeira letre A apareceu na posicão {}'.format(nome.upper().find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.upper().rfind('A')+1))


print('=' * 40)


