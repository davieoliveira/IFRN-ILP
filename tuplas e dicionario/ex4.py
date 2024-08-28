numeros = [1, 2, 3, 4, 5, 6]
letras = ['a', 'b', 'c', 'd', 'e','f']
saida = ''

for x in range(len(numeros)):
    if x % 2 == 0:
        saida += str(numeros[x]) + ' '
    else:
        saida += str(letras[x]) + ' '

print(saida)