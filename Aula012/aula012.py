print (' ')
print('=' * 40)
nome = str(input('\033[31m Qual é o seu nome? \033[m'))
print('=' * 40)  
if nome == 'João':
    print('\033[32m Que nome bonito! \033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil! {}. '.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal !')
print('\033[34mTenha um bom dia {}! \033[m' .format(nome))
print (' ')

# o else é opcional para terminar uma estrutura condicional aninhada.

