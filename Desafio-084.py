# Iniciação das variáveis
listaGeral = []
listaAuxiliar = []
cont = maiorPeso = menorPeso = 0

while True:
    # Entrada de dados
    nome = str(input('Nome: '))
    listaAuxiliar.append(nome)
    peso = float(input('Peso: Kg'))
    listaAuxiliar.append(peso)
    listaGeral.append(listaAuxiliar[:])  # Faz uma copia da listaAuxiliar para listaGeral
    listaAuxiliar.clear()  # Limpa a lista auxiliar

    # Processamento de dados
    if cont == 0:
        menorPeso = maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if menorPeso > peso:
            menorPeso = peso
    cont += 1

    # Artificio de saída do laço infinito
    while True:
        varControle = str(input('Deseja continuar? [S/N]')).upper()[0]
        if varControle in 'SN':
            break
    if varControle in 'N':
        break

# Saída de dados
print(f'Foram cadastrado {cont} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for p in listaGeral:
    if maiorPeso == p[1]:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end=' ')
for p in listaGeral:
    if menorPeso == p[1]:
        print(f'[{p[0]}]', end=' ')
print()
