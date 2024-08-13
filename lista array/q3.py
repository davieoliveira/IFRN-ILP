# leia 10 valores inteiros e armazene em uma lista. O programa deve 
# imprimir no terminal quantos valores pares foram digitados pelo 
# usuário. Dica: use o operador “%” para verificar se o número é 
# par (ZERO é neutro, ZERO NÃO É PAR). Exemplos:
contador_par = 0
for x in range(0, 10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0 and numero != 0:
        contador_par += 1
    
print(f'Foram encontrados {contador_par} pares')