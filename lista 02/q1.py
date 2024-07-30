# 1. Crie um programa que leia o salário de uma pessoa e calcule o imposto de renda a
# ser pago baseado nas seguintes faixas: até R$ 1.903,98 isento, de R$ 1.903,99 até
# R$ 2.826,65 o imposto é de 7,5%, de R$ 2.826,66 até R$ 3.751,05 o imposto é de
# 15%, de R$ 3.751,06 até R$ 4.664,68 o imposto é de 22,5%, acima de R$ 4.664,68
# o imposto é de 27,5%

salario = float(input('Digite o valor de seu salário: '))
taxa = 0

if salario <= 1903.98:
    print('insento de imposto de renda.')

elif salario > 1903.98 and salario <= 2826.65:
    taxa = salario * 0.075
    print(f"O imposto será de {taxa:.2f} R$")

elif salario > 2826.65 and salario <= 3751.05:
    taxa = salario * 0.15
    print(f"O imposto será de {taxa:.2f} R$")

elif salario >= 3751.06 and salario <= 4664.68:
    taxa = salario * 0.225
    print(f"O imposto será de {taxa:.2f} R$")

elif salario > 4664.68:
    taxa = salario * 0.275
    print(f"O imposto será de {taxa:.2f} R$")

else:
    print('Valor inválido!')