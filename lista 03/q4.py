# 4. Escreva um algoritmo que solicite do usuário 10 números e ao final imprima na tela o
# somatório desses números.
soma_total = 0
for x in range(0, 10):
    number = int(input('Digite um valor: '))
    soma_total += number
print(soma_total)