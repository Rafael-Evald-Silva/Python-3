# Variáveis
valores = []

# Entrada de dados
for c in range(0, 5):
    num = int(input('Digite um valor: '))

    # Processamento de dados
    if c == 0:
        valores.append(num)
        print('Adicionado ao final da lista.')
    elif num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

# Saída de dados
print(f'A lista de valores digitados em ordem é {valores}')
