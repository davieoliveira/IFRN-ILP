# 1. Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e remova todos os elementos duplicados, mantendo a
# ordem original dos elementos. Ao final, apresente os valores fornecidos
# pelo usuário e o resultado do processamento da sua solução;
lista_numeros_inteiros = [1, 1, 40, 1, 2, 4, 10, 50, 40, 10, 1]
nova_lista = []
for numero in range(0, len(lista_numeros_inteiros)):
    if lista_numeros_inteiros[numero] not in nova_lista:
        nova_lista.append(lista_numeros_inteiros[numero])
print(nova_lista)