# Escreva um programa que receba como entrada uma sequência de valores 
# inteiros. Para tanto, o programa deverá inicialmente solicitar ao usuário 
# quantos valores serão fornecidos para análise e só depois solicitar os 
# valores a serem analisados. A análise consistirá em identificar e apresentar 
# a partir da sequência de valores fornecidos, o menor valor, o maior valor e 
# a média aritmética dos valores. Exemplos:
menorValor = 100000000
maiorValor = -100000000
somaTotal = 0
array = [10, 40, 13]

for x in range(0, len(array)):
    if ( array[x] > maiorValor ):
        maiorValor = array[x]

    if ( array[x] < menorValor ):
        menorValor = array[x] 
    
    somaTotal += array[x]

media = somaTotal/len(array)
print(f'O maior valor foi {maiorValor}, e o menor foi {menorValor} e a media foi de {media}')