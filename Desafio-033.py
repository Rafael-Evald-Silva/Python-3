# Variaveis
cont = 0
maior = 0
menor = 0

# Entrada e processamento de dados
while True:
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    if cont == 3:
        break

# Saida de dados
saida = ' Resultados '
print(f'{saida:=^30}')
print(f'O maior número digitado foi {maior}.')
print(f'O menor número digitado foi {menor}.')
