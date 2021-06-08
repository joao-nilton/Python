print (' ')
print('=--=' * 20)
print('RADAR ELETRÔNICO')
print('=--=' * 20)
print(' ')
print('+--+' * 20)
print (' ')

num = int(input('Qual é a velocidade atual do carro? '))




num1 = num - 80



if num <= 80:
    print('Tenha um bom dia! Dirija com segurança')
elif num <= 100:
    vm = int(input('Qual é o valor da multa por quilômetro excedido: '))
    num2 = num1 * vm
    print('Você excedeu o limite de velocidade que é de 80Km/h')
    print('Voce deve pagar uma multa de  R$: {}'.format(num2))
    
else:
    vm1 = int(input('Qual é o valor da multa por quilômetro excedido acima de  100Km/h: '))
    num3 = num1 * vm1
    print('Você excedeu o limite de velocidade que é de 80Km/h')
    print('Voce deve pagar uma multa de  R$: {}'.format(num3))
print (' ')