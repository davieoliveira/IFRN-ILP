# 2. Escreva um programa que recebe como entrada valores inteiros para criar 
# duas listas de mesmo tamanho. O tamanho das listas deverá ser definido pelo 
# usuário. O programa deverá somar os valores pares e ímpar de cada uma das 
# listas. Em seguida, comparar as somas e informar qual dos somatórios é maior 
# ou se há um empate. Exemplos:
tamanho_listas = int(input('Quantos números deverão haver na lista: '))
soma_par_1 = 0
soma_par_2 = 0
soma_impar_1 = 0
soma_impar_2 = 0

lista1 = []
lista2 = []

for x in range(0, tamanho_listas):
    novo_numero_1 = int(input('Digite um número para a lista A: '))
    novo_numero_2 = int(input('Digite um número para a lista B: '))

    lista1.append(novo_numero_1)
    lista2.append(novo_numero_2)


for x in range(0, tamanho_listas):
    if ( lista1[x] % 2 == 0 ):
        soma_par_1 += lista1[x]
    
    if ( lista1[x] % 2 != 0 ):
        soma_impar_1 += lista1[x]

    if ( lista2[x] % 2 == 0 ):
        soma_par_2 += lista2[x]

    if ( lista2[x] % 2 != 0 ):
        soma_impar_2 += lista2[x]
    
print(f'Soma listaPar1: {soma_par_1}')
print(f'Soma listaPar2: {soma_par_2}')

if ( soma_par_1 < soma_par_2 ):
    print(f'listaPar1 < listaPar2')
elif( soma_par_1 > soma_par_1):
    print('somaPar1 > somaPar2')
else:
    print('somaPar1 == somarPar2')


print(f'Soma listaImpar1: {soma_impar_1}')
print(f'Soma listaPar2: {soma_impar_2}')

if ( soma_impar_1 < soma_impar_2 ):
    print(f'listaimpar1 < listaImpar2')
elif( soma_impar_1 > soma_impar_2):
    print('SomaImpar1 > somaImpar2')
else:
    print('SomaImpar1 == somarImpar2')