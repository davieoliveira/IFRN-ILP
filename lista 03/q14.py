# 14. Escreva um algoritmo que solicite ao usuário um número inteiro e depois imprima uma
# sequência de caracteres que represente um triângulo. Exemplo: 
numero = int(input("Digite um número inteiro: "))

for i in range(1, numero + 1):
    print('* ' * i)

for i in range(numero - 1, 0, -1):
    print('* ' * i)
