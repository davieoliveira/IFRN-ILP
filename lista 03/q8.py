# 8. Escreva um algoritmo que solicite do usuário um número correspondente à quantidade
# de valores que o usuário fornecerá para o algoritmo. Ao final, o algoritmo deverá informar
# quantos números pares foram digitados.
contador_de_pares = 0
quantidade_numeros = int(input('Digite quantos numeros você deseja contar: '))
for x in range(1, quantidade_numeros+1):
    if x % 2 == 0:
        contador_de_pares += 1
print(f'Foram encontrados {contador_de_pares} números pares.')