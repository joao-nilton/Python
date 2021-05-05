print('Este é um conversor de medidas de comprimento') 
m = float(input('Digite o valor que quer em metros da medida que quer converter: '))
km = m * 0.001
cm = m * 100
mm = m *1000
inch = m * 39.3701

print(' {} metro(s) corresponde a {} Km(s)'. format(m, km)) 
print(' {} metro(s) corresponde a {} cm(s)'. format(m, cm)) 
print(' {} metro(s) corresponde a {} mm(s)'. format(m, mm)) 
print(' {} metro(s) corresponde a {} polegada(s)'. format(m, inch)) 
