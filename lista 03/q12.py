# 12. Escreva um algoritmo que imprima na tela todos os números divisíveis por 7 (separados por “;”), 
# mas que não sejam múltiplos de 5 no intervalo de 1000 a 3000. 
for i in range(1000, 3000):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=';')