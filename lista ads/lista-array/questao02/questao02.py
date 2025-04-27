array_a = []
contador_impar = 0

for x in range(0, 5):
    number = int(input("Digite um número: "))
    array_a.append(number)

for number in array_a:
    if number % 2 != 0:
        contador_impar += 1

print(contador_impar)