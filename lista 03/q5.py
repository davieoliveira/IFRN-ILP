# 5. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores menores que 10.
soma_total = 0;
for x in range(0, 5):
    number = int(input("Digite um valor: "))
    if number < 10:
        soma_total += number