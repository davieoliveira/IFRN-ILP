# Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e utilize uma list comprehension para gerar uma nova lista contendo
# os quadrados de todos os números ímpares da lista original.

array_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista_numeros = [numero*numero for numero in array_numeros if numero % 2 != 0]
print(nova_lista_numeros)