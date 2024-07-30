# 15. Escreva um algoritmo que solicite números ao usuário e conte quantos desses são
# pares e quantos são ímpares, até que seja digitado um número negativo. Ao final 
# imprima na tela quantos números pares e ímpares foram digitados. 
numeros_pares = 0
numeros_impares = 0
numero = 1

while (numero > 0):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f'Pares = {numeros_pares}, impares = {numeros_impares}')