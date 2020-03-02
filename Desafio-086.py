# Declaração da lista
matrizLista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Entrada de dados
for l in range(0, 3):
    for c in range(0, 3):
        matrizLista[l][c] = int(input(f'Digite um valor para:[{l}, {c}] '))

# Saída de dados
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matrizLista[l][c]:^5} ]',end='')
    print()
