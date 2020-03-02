# Iniciando as variáveis
litas = []
cont = 0

while True:  # inicio do laço infinito
    # Entrada de dados
    num = int(input('Digite um valor: '))
    litas.append(num)

    # Saída do laço infinito
    while True:
        varContro = str(input('Deseja inserir mais valores? [S/N]')).upper()[0]
        if varContro in 'SN':
            break
    if varContro == 'N':
        break
# Processamento de dados
litas.sort(reverse=True)    # Deixa os valores em ordem decrecente.
for val in litas:
    if val == 5:
        cont += 1

# Saída de dados
print('=' * 40)
print(f'Foram digitados {len(litas)} número.')
print(f'A lista de valores em ordem decrecente é {litas}')
if cont > 0:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não esta na lista.')
