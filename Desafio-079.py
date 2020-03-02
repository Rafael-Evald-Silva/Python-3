# Declaração de variáveis
valores = []
cont = cont3 = 0

# Entrada de dados
while True:
    print(f'{" Entrada de dados ":=^50}')
    num = int(input('Digite um valor na Lista: '))

    # Processamento de dados
    if cont == 0:
        valores.append(num)
        print('Valor cadastrado com sucesso.')
    else:
        # Verifica se ja existe um valor na lista
        for val in valores:
            if val == num:
                cont3 += 1
        # Adiciona o valor a lista caso o mesmo não exista
        if cont3 == 0:
            valores.append(num)
            print('Valor cadastrado com sucesso.')
        else:
            print('O valor ja existe na lista.')
    cont += 1   # Contador para adicionar  lista o primeiro valor.
    cont3 = 0   # Contador para verificar se ja existe um valor na lista.

    # Condição de saída do laço - Inicio
    print('-' * 50)
    while True:
        varControle = str(input('Deseja colocar mais valores na Lista? [S/N]')).upper()[0]
        if varControle in 'SN':
            break
    if varControle == 'N':
        break
    print('=' * 50)
    # Condição de saída do laço - Fim

# Saída de dados - Inicio
print(f'{" O resultados ":=^50}')
print(f'Os valores digitados foram {sorted(valores)}.')
print('=' * 50)
# Saída de dados - Fim
