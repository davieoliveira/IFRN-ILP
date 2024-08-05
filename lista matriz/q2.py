# Escreva um programa que leia uma lista de números inteiros fornecida 
# pelo usuário e um número alvo. O programa deve encontrar todos os
# pares de números na lista cuja soma seja igual ao número alvo.
lista_numeros_inteiros = [2, 4, 3, 5, 7]
lista_de_pares = []
numero_alvo = int(input('Digite um número alvo:\n'))
print('Digite 10 números inteiros: ')

# Encontrando os pares somados que resultam em um número alvo
for x in range(0, len(lista_numeros_inteiros)):
    for y in range(0, len(lista_numeros_inteiros)):
        if(lista_numeros_inteiros[x] + lista_numeros_inteiros[y] == numero_alvo):
            if([lista_numeros_inteiros[x], lista_numeros_inteiros[y]] not in lista_de_pares and [lista_numeros_inteiros[y], lista_numeros_inteiros[x]] not in lista_de_pares):
                lista_de_pares.append([lista_numeros_inteiros[x], lista_numeros_inteiros[y]])
print(lista_de_pares)