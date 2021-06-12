print (' ')
print('=--=' * 20)
print('Programa que lê três números e mostra qual é o maior e qual é o menor')
print('=--=' * 20)

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro  número: '))
print (' ')

maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior: ',maior)

    # Achando o menor número
menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro

print('Menor: ',menor)

    # Esse tá difícil eu copiei