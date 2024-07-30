# 9. Escreva um algoritmo que solicite do usuário 10 valores. O algoritmo deverá calcular
# a soma da sequência de valores pares e dos valores ímpares, ou seja, somar o 1º
# número digitado com o 3º, 5º, 7º e 9º e o mesmo para os números pares. Após, informar
# e o somatório dos números ímpares é maior, igual ou menor do que o dos números
# pares.
soma_pares = 0
soma_impares = 0

for x in range(1, 11):
    numero = int(input('Digite um número: '))
    if(x % 2 == 0):
        soma_pares += numero
    else:
        soma_impares += numero

print(f'Soma dos números par:{soma_pares}, impar:{soma_impares}')

if(soma_impares > soma_pares):
    print('A soma dos números impares é maior que dos pares')
elif(soma_impares == soma_pares):
    print('A soma dos impares foi igual a soma dos pares')
else:
    print('A soma dos impares foi menor que a dos pares.')

