# 6. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores maiores ou igual a 10 e menor do que 20.
somatorio = 0
for x in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero >= 10 and numero < 20:
        somatorio += numero
print(f'a soma dos números maiores ou igual a 10 e menores que 20 resultou em {somatorio}')