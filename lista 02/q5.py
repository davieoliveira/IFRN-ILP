# 5. Escreva um programa que leia dois valores inteiros e escreva como saída a diferença
# entre o maior valor e o menor valor.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    print(f'A diferença entre o valor {valor1} pro valor {valor2} é de {valor1-valor2}')
elif valor2 > valor1:
    print(f'A diferença entre o valor {valor2} pro valor {valor1} é de {valor2-valor1}')
else:
    print('Os valores são iguais')