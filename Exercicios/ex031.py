print (' ')
print('=--=' * 20)
print('PREÇO DA PASSAGEM RODOVIÁRIA')
print('=--=' * 20)

'''num = float(input('Qual a distância de sua viagem? '))


if num <= 200:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num1 = num * 0.50
    print('E o preço da passagem é de {} Reais'.format(num1))
else:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num2 = num * 0.45
    print('E o preço da passagem é de {} Reais'.format(num2))'''

print('OU...')

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a iniciar uma viagem de {}Km'.format(distancia))
preco = distancia * .50 if distancia <= 200 else distancia * .45
print('E o preço de sua passagem sera de R$ {:.2f}'.format(preco))

print (' ')
