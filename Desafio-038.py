# Entrada de dados
numeros = []
cont = 0
while True:
    num = int(input(f'Digite o valor {cont+1}: '))
    numeros.append(num)
    cont += 1
    if cont == 2:
        break

# Saída de dados
if numeros[0] > numeros[1]:
    print('O PRIMEIRO valor é maior.}')
elif numeros[1] > numeros[0]:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são iguais.')
