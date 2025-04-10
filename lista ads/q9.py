# Escreva um algoritmo que receba um array A de n números naturais e determine se o array está ordenado em
# ordem não decrescente, ou seja, do menor para o maior.
arrayA = [1,2,3,4,5,6]
crescenete = True

for x in range(0, len(arrayA) - 1):
    if arrayA[x] > arrayA[x+1]:
        crescenete = False
        break

print(crescenete)
        