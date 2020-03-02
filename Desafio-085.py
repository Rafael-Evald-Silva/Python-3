# Declarando listas
listaParImpar = [[], []]

# Corpo do programa
for c in range(0, 7):
    # Entrada de dados
    num = int(input(f'Digite o {c + 1}ª valor: '))

    # Processamento de dados
    if num % 2 == 0:
        listaParImpar[0].append(num)
    else:
        listaParImpar[1].append(num)

# Processamento de dados
parOrdenado = sorted(listaParImpar[0])
imparOrdenado = sorted(listaParImpar[1])

# Saída de dados
print(f'A listar par e {parOrdenado}')
print(f'A listar impar é {imparOrdenado}')
