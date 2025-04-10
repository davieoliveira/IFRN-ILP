numero = int(input("Digite um número para saber se ele é primo."))
quantidade_divisores = 0

for x in range(1, numero +1):    
    if numero % x == 0:
        quantidade_divisores += 1

if quantidade_divisores == 2:
    print('o número é primo')
else:
    print('o número não é primo')