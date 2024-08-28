# Como preencher uma matriz.

# criando uma matriz
matriz = [[0 for x in range(3)] for y in range(3)]

# Preenchendo a matriz
for x in range(0, 3):
  for y in range(0, 3):
    matriz[x][y] = int(input(f'Digite o valor do espaço [{x+1}, {y+1}] da matriz: '))

# Exiibidno
for linha in matriz:
  print(linha)
