print("\n" * 1)
print('=' * 40)
print('Conversor de temperatura ') 
print('=' * 40)
print("\n" * 1)

v = float(input('Digite o valor da temperatura em graus celsius: '))
f =  (v * 9/5)+ 32
k =  v + 273.15

print('O valor da temperatura em Fahrenheit e {} Fº '.format(f))
print('O valor da temperatura em Kelvin e {} Kº '.format(k))
print("\n" * 1)
print('=' * 40)