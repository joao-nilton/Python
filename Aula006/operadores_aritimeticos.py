# import numpy as np
# from numpy import log as ln

n1 = int(input( 'Digite o primeiro valor:  '))
n2 = int(input( 'Digite o segundo valor:  '))
s = n1 + n2
ss = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
r = m ** (1/2)
# inve = log(e,2)

print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}, a divisão inteira é  {}, o resto da divisão é {}, a exponencial é {} e a raiz quadrada {}'.format (s, ss, m, d, di, dr, e, r))

# poderia ter divido as respostas em mais print.  \n quebra o print e end=' ' emenda no final