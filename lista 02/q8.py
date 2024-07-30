# 8. Escreva um programa que leia três valores e determine se eles podem formar um
# triângulo. Caso possam, classifique o triângulo como equilátero, isósceles ou escaleno.

ladoa = int(input('Digite o lado a: '))
ladob = int(input('Digite o lado b: '))
ladoc = int(input('Digite o lado c: '))
if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    if ladoa == ladob and ladoc == ladob:
        print('O triângulo é equilátero.')
    if ladoa != ladob and ladob != ladoc:
        print('O triângulo é escaleno.')
    if ladoa == ladob and ladoa != ladoc or ladob == ladoc and ladoc != ladoa:
        print('O triângulo é isosceles')
else:
    print('Não é um triângulo.')