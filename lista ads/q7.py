numero_alvo = int(input("Digite um número para achar no array números somados que resultaram nele: "))
array_a = [3, 1, 7, 9, 5]
condicao = False

for x in range(0, len(array_a)):
    for y in range(x + 1, len(array_a)):
        if array_a[x] + array_a[y] == numero_alvo and x != y:
            condicao = True

print(condicao)
