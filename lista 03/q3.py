# 3. Escreva um algoritmo que solicite ao usuário dois valores para determinação de um
# intervalo. Ao final o algoritmo deverá imprimir todos os números desse intervalo e o
# somatório deles.
number1 = int(input('Digite o primeiro valor: '))
number2 = int(input('Digite o segundo valor: '))
soma_total = 0
for x in range(number1, number2):
    print(x)
    soma_total += x
print(soma_total)
