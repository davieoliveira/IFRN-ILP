# 16. Escreva um algoritmo que solicite ao usuário um valor e em seguida apresente na tela 
# uma sequência começando em 1 e indo até o valor fornecido pelo usuário. Porém, se 
# nessa sequência houver um número que seja múltiplo de 3 escreva PI, e se houver 
# um número que seja múltiplo de 7 escreva PA. Caso haja um número que seja múltiplo
# de 3 e 7 escreva POW.
numero = int(input('Digite um valor: '))

for x in range(1, numero + 1):
    if x % 3 == 0 and x % 7 == 0:
        print('POW')
    elif x % 3 == 0:
        print('PI')
    elif x % 7 == 0:
        print('PA')    
    else:
        print(numero)