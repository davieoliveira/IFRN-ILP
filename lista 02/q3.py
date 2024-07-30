# 3. Escreva um programa que solicite um número entre 1 e 10. Caso o usuário digite um
# valor dentro dessa faixa o programa deverá exibir a mensagem “O número digitado
# está DENTRO da faixa solicitada.”, senão o programa deverá exibir a mensagem “O
# número digitado está FORA da faixa solicitada.”.
numero = int(input('Digite um número de 1 a 10: '))
if(numero >= 1 and numero <= 10):
    print(f'O número {numero} está dentro da faixa solicitada.')
else:
    print(f'O número {numero} está fora da faixa solicitada.')