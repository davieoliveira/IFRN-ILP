# 10. Escreva um algoritmo que solicite do usuário 10 valores inteiros. O algoritmo deverá
# calcular o somatório dos números pares e dos números ímpares que forem digitados
# pelo usuário. Após o somatório, o algoritmo deve informar se o somatório dos números
# ímpares é maior, igual ou menor do que o dos números pares.
soma_pares = 0
soma_impares = 0

for x in range(0, 11):
    numero = int(input('Digite o número: '))
    
    if numero % 2 == 0 :
        soma_pares += numero
    else:
        soma_impares += numero

if(soma_impares > soma_pares):
    print('A soma dos números impares foi amor')

elif(soma_impares == soma_pares):
    print('A soma dos impares foi igual a soma dos pares')
else:
    print('A soma dos números pares foi maior')

