# Declaração da matriz
matriz = [[], [], []]
# Iniciando as variáveis
somaPar = somaColuna = maiorValor = 0

# Entrada de dados - Inicio
for d in range(0, 3):
    num = int(input(f'Digite um valor na posição [0, {d}] '))
    matriz[0].append(num)
for d in range(0, 3):
    num = int(input(f'Digite um valor na posição [1, {d}] '))
    matriz[1].append(num)
for d in range(0, 3):
    num = int(input(f'Digite um valor na posição [2, {d}] '))
    matriz[2].append(num)
# Entrada de dados - Fim

# Processamento de dados - Inicio
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somaPar = somaPar + matriz[l][c]

for l in range(0, 3):
    somaColuna = somaColuna + matriz[l][2]

for l in range(0, 3):
    if matriz[1][l] == 0:
        maiorValor = matriz[1][l]
    else:
        if matriz[1][l] > maiorValor:
            maiorValor = matriz[1][l]
# Processamento de dados - Fim

# Saída de dados - Inicio
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print('\n', end='')
print('-=' * 20)
print(f'A soma de todos os valores pares digitados é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda linha é {maiorValor}.')
# Saída de dados - Fim
