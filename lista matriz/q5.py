m = int(input('Digite o tamanho m da matriz: '))
n = int(input('Digite o tamanho n da matriz: '))
matriz = []
for x in range(n):
    for y in range(m):
        novo_indice = int(input('Digite um valor: '))
        matriz.append([novo_indice])

for linha in matriz:
    print(linha)