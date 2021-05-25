# Fatiamento
frase = '   Curso em vídeo python   '
print(frase)
print(frase[9]) # imprime o caractere da posição 10.
print(frase[9:13]) # imprime o carectere de 10 a 12.
print(frase[9:21:2]) # imrime os caracteres de 9 a 20 pulando de 2 em 2.
print(frase[:5]) # começa do caractere zero até o caractere 4.
print(frase[15:]) # começa do quinze e vai até o final. Se nao tiver caractere suficiente a partir do início selecionado o python retorna uma linha vazia.
print(frase[9::3]) # começa no 9 até o final de 3 em 3.
print(frase[::2]) # imprime do inicio ao fim saltando de 2 em 2.
print('oi')



# 2. Análise de string

print(len(frase)) # comprimento da frase
print(len(frase.strip()))
print(len(frase.rstrip()))
print(len(frase.lstrip()))
print(frase.count('o')) # quantas vezes aparece a letra o minuscula.
print(frase.count('o',0,13)) # considera do 0 atér o 12
print(frase.find('deo')) # onde ocorre o inicio de deo
print(frase.find('ANDROID')) # => -1 -> Ess string androide nao existe na string curso em video
print('Curso'in frase) # retorna True

# 3. Funcionalidades

# 3.1 trasnsformação. Consegue-se mudar atraves dos métodos, mas não pelos elementos
print(frase.replace('python','Android'))
print(frase.upper()) # () <=> método
print(frase.upper().count('O')) # pega a frase, joga pra maiúscula e  conta quantas vezes tem o O maiúsculo 
print(frase.lower())
print(frase.capitalize()) # Maiúscula sempre a :etra inicial colocando as outras em minúscula -> Curso em vídeo
print(frase.title()) # analisa os espaços e capitaliza antes de espaço -> Curso Em Video
print(frase.strip()) # remove espaços inúteis no início e fim da frase.
print(frase.rstrip()) # inúteis a direita.
print(frase.lstrip()) # inúteis a esquerda.

# 3.2 Divisão
print(frase.split()) # divide a string a partir dos espaços entre as palavras.
 # print(frase.join(frase)) # junta palavras espaçadas com um traço.

# PS - para imprimir trecho de textos usa-se 3 aspas Ex: print ("""" AS Minsas do rei ....(muito texto) """)

frase1 = "Curso em vídeo"
print(frase1.replace('vídeo','áudio'))
print(frase1)

frase3 = 'Curso em vídeo POO'
dividido = frase3.split()
print(dividido[0])
print(dividido[0][4])