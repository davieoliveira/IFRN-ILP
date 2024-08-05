# Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e um número de passos. O programa deve rotacionar a lista para a
# direita pelo número de passos especificado.
array = [1, 2, 3, 4, 5]
numero_passos = 2
lista_rotacionada = []

for x in range(0, len(array)):
    lista_rotacionada.append(array[x - numero_passos])

print(lista_rotacionada)