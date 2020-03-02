# Entrada de dados
numero = int(input('Digite o número que deseja ver a tabuada: '))
cont = 1

# Processamento
print('-=-=' * 5)
while True:
    print(f'{numero} x {cont:2} = {numero * cont}')
    cont += 1
    if cont == 11:
        break
print('-=-=' * 5)
