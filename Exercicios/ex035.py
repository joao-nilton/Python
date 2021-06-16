'''Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.'''

print (' ')
print('=--=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('=--=' * 20)


lado1 = float(input('Digite o primeiro número: '))
lado2 = float(input('Digite o segundo número: '))
lado3 = float(input('Digite o terceiro  número: '))

if lado1 > ((lado2 - lado3) or (lado3 - lado2)):

 if lado1 < ((lado2 + lado3) or (lado3 +lado2)):
 
    if lado2 > ((lado1 - lado3) or (lado3 - lado1)):
    
        if lado2 < ((lado1 + lado3) or (lado3 +lado1)):
   
            if lado3 > ((lado2 - lado1) or (lado1 - lado2)):

                if lado3 < ((lado2 + lado1) or (lado1 +lado2)):

                    print (' ')
                    print ('Os valores {}, {} e {} formam um triângulo'.format(lado1, lado2, lado3))
                    print (' ')

                else:
                    print (' ')
                    print ('Os valores {}, {} e {} não formam um triângulo'.format(lado1, lado2, lado3))
                    print (' ')