import math

a = float(input(''))
b = float(input(''))
c = float(input(''))

delta = (b**2 - 4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular o valor das raizes.')
else:
    raiz_1 = (-b + math.sqrt(delta)) / (2*a)
    raiz_2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'R1 = , {raiz_1:.5f}')
    print(f'R1 = , {raiz_2:.5f}')
