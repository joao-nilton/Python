print (' ')
print('=--=' * 20)
print('PREÇO DA PASSAGEM RODOVIÁRIA')
print('=--=' * 20)

num = float(input('Qual a distância de sua viagem? '))


if num <= 200:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num1 = num * 0.50
    print('E o preço da passagem é de {} Reais'.format(num1))
else:
    print('Você está prestes a iniciar uma viagem de {} Km'.format(num))
    num2 = num * 0.45
    print('E o preço da passagem é de {} Reais'.format(num2))
    
print (' ')
