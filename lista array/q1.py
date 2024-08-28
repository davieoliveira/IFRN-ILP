# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. 
# O programa deve imprimir no terminal quantos valores pares foram digitados pelo usuário.
# Dica: use o ope rador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR). Exemplos:
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_de_par = 0

for x in range(0, len(lista_numeros)):
    if( lista_numeros[x] % 2 == 0 and lista_numeros[x] != 0):
        contador_de_par += 1

print(f'Foram encontrados {contador_de_par} números par.')