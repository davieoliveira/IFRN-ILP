# Escreva um programa que receba como entrada uma string constituída 
# por uma sequência de números inteiros separados por espaço. O programa 
# deverá transformar essa string em uma lista de números inteiros e 
# apresentar o resultado da soma dos valores das posições ímpares dessa 
# lista. Exemplos:
numeros = input('Digite os números: ')
saida = ''
soma_impares = 0

for x in range(0, len(numeros)):
    if x % 2 != 0:
        soma_impares += int(numeros[x])
        saida += numeros[x] 

print(saida, soma_impares) 