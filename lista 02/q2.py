# 2. Escreva um programa que solicita o valor de um ano ao usuário, em seguida informa
# se o ano fornecido é ou não bissexto. [Dica: um ano é bissexto se é divisível por 4,
# mas não por 100. Para que um número X seja considerado divisível por um número
# Y é preciso que o resto da divisão de X por Y seja igual a ZERO].

ano = int(input('Digite um ano: '))

if( ano % 4 == 0 and ano % 100 != 0):
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')