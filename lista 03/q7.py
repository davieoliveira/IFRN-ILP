# 7. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores pares que foram digitados.
soma_valores = 0
for x in range(0,5):
    number = int(input('Digite um valor: '))
    if number % 2 == 0:
        soma_valores += number
print(soma_valores)