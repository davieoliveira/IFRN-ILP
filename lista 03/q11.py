# 11. Escreva um algoritmo que informe ao usuário que calcula o somatório de uma sequência de números. 
# O algoritmo deverá solicitar ao usuário o total de números que deverão ser somados. Depois o algoritmo 
# deve realizar a soma de todos os números e apresentar na tela o resultado dessa soma conforme exemplo abaixo:
# Digite o total de números a serem somados: 5
# 2 7 3 8 6 (números digitados pelo usuário)
# Saída no terminal: 2+7+3+8+6=26

numero_de_somas = int(input('Quantos números você deseja somar: '))
soma_total = 0
texto_final = ''
for x in range(0, numero_de_somas):
    numero = int(input('Digite um número: '))

    if x == numero_de_somas - 1:
        soma_total += numero
        texto_final += f'{numero} = {soma_total}'
        print(texto_final)

    texto_final += f'{numero} + '
    soma_total += numero