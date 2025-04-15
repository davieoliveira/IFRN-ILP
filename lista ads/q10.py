a = [10, 5, -17, 20, 50, -1, 3, -30, 10]
maior_soma = a[0] 

for x in range(len(a)):
    soma_atual = 0
    for y in range(x, len(a)):
        soma_atual += a[y] 
        if soma_atual > maior_soma:
            maior_soma = soma_atual

print(maior_soma)  