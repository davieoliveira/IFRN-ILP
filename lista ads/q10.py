# Problema Sublista contígua de soma máxima.
# Considere um array A de n números inteiros. Exemplo: A = [10, 5, −17, 20, 50, −1, 3, −30, 10]
# O problema consiste em encontrar a maior subsequencia cuja soma seja a maior possível. No caso do vetor A a
# maior soma é 72, que é a soma dos elementos entre os índices 3 e 6 : 20 + 50 + −1 + 3.
# (20 + 50 -1 + 3 = 72) Maior soma possivel.

a = [10, 5, -17, 20, 50, -1, 3, -30, 10]
maior_soma = a[0] 

for x in range(len(a)):
    soma_atual = 0
    for y in range(x, len(a)):
        soma_atual += a[y] 
        if soma_atual > maior_soma:
            maior_soma = soma_atual

print(maior_soma)  