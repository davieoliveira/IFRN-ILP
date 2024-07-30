# 6. Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida 
# o programa deverá exibir os 3 valores digitados pelo usuário em ordem crescente.
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

if valor1 <= valor2 and valor1 <= valor3:
    if valor2 <= valor3:
        print(valor1, valor2, valor3)
    else:
        print(valor1, valor3, valor2)

elif valor2 <= valor1 and valor2 <= valor3:
    if valor1 <= valor3:
        print(valor2, valor1, valor3)
    else:
        print(valor2, valor3, valor1)

else:
    if valor1 <= valor2:
        print(valor3, valor1, valor2)
    else:
        print(valor3, valor2, valor1)
