# Considere um array A de n números naturais Ai. Escreva um algoritmo que determine a maior diferença absoluta
# um par de elementos consecutivos da lista.
# O algoritmo deve retornar o valor da diferença.
# Exemplo: Para o array A = [9, 5, 8, 2, 1, 3, 5, 9, 4, 1], onde os índice são numerados de 0 a 9, da esquerda 
# para a direita, a maior diferença absoluta é 6, obtida a partir dos elementos consecutivos 8 e 2, nos índice 
# 2 e 3, respectivamente.

a = [9, 5, 8, 2, 1, 3, 5, 9, 4, 1]
maior_diferenca = 0  
for i in range(len(a) - 1):  
    diferenca = a[i] - a[i + 1] 
    if diferenca > maior_diferenca:
        maior_diferenca = diferenca  

print(maior_diferenca)  