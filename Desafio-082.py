# Iniação das variáveis
Lista = []
ListaPar = []
ListaImpar = []

while True:
    # Entrada de dados
    num = int(input('Digite um número: '))
    Lista.append(num)

    # Artificio de saída do laço infinito
    while True:
        varControle = str(input('Deseja continuar? [S/N]')).upper()[0]
        if varControle in 'SN':
            break
    if varControle in 'N':
        break

# Processamento de dados
for val in Lista:
    if val % 2 == 0:
        ListaPar.append(val)
    else:
        ListaImpar.append(val)

# Saída de dados
print(f'Os valores da Lista principal é {Lista}.')
print(f'Os valores da Lista Par é {ListaPar}.')
print(f'Os valores da Lista IMpar é {ListaImpar}.')
