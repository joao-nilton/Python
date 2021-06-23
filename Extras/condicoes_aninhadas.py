print (' ')
print('=' * 312)
print('\033[1;31m TTITULO DO PROGRAMA \033[m')
print('=' * 312)  
print (' ')
nome = str(input('\033[31mQual é o seu nome? \033[m'))
if nome == 'João':
    print('\033[32mQue nome bonito! \033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil! {}. '.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal !')
print('\033[34mTenha um bom dia {}! \033[m' .format(nome))
print (' ')

# o else é opcional para terminar uma estrutura condicional aninhada.

'''
import unicodedata
import re

def removerAcentosECaracteresEspeciais(palavra):

   # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)'''
    
