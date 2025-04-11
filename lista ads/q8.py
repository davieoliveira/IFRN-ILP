# Considere um array A de n números naturais Ai e s um valor natural. Escreva um algoritmo que verfique quantos
# pares de elementos em A cuja soma seja s existem.
# O algoritmo deve retornar um valor inteiro, a quantidade de pares cuja soma seja s

numero_alvo = 12
array_a = [4, 7, 11, 8, 1, 3]
pares_encontrados = []
quantidade_pares = 0

for x in range(0, len(array_a)):
    for y in range(x + 1, len(array_a)):
        if array_a[x] + array_a[y] == numero_alvo and x != y:
            pares_encontrados.append([array_a[x], array_a[y]])
            quantidade_pares += 1
            
print(pares_encontrados)
print(quantidade_pares)