from random import shuffle

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

palavras = [a1, a2, a3, a4 ]

shuffle(palavras)

print (' ')
print('Os (As) aluno(s)(as) apresentarão na seguintre sequência {}: '.format(palavras))
#print('A ordem de apresentação será {}: '.format(sequencia))