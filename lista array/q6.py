# 6. Crie um programa que solicite ao usuário uma lista de números 
# inteiros e uma string de mesmo comprimento. O programa deve 
# substituir os números nos índices ímpares da lista por caracteres 
# correspondentes da string nos mesmos índices. Exiba a sequência 
# resultante, separada por um espaço em branco. Exemplo:

numeros = 1, 2, 3, 4, 5, 6
letras = 'abcdef'
novoArray = []

for x in range(0, len(numeros)):
    if x % 2 == 0:
        novoArray.append(numeros[x])
    else:
        novoArray.append(letras[x])

print(novoArray)