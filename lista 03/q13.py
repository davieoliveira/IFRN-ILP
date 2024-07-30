# 13. Escreva um algoritmo que imprima na tela a tabuada da multiplicação de um número
# inteiro de 1 a 10. Exemplo:
# Entrada: 9
# Saída: 1x9=9; 2x9=18; 3x9=27; 4x9=36; 5x9=45; 6x9=54; 7x9=63; 8x9=72;
# 9x9=81; 10x9=90;

numero = int(input('Digite o número para exibir a tabuada: '))
for x in range(1, 11):
    print(f'{numero} x {x} = {numero*x}')