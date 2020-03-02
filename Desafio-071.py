# Entrada de dados - Begin
print('=' * 50)
valor = int(input('Deseja sacar quantos R$'))
# Entrada de dados - End

# Iniciando variável cont
cont50 = cont20 = cont10 = cont1 = cont100 = 0

# Processamento de dados- Begin
while True:
    if valor % 100 == 0:
        valor = valor - 100
        cont100 += 1
    elif valor % 50 == 0:
        valor = valor - 50
        cont50 += 1
    elif valor % 20 == 0:
        valor = valor - 20
        cont20 += 1
    elif valor % 10 == 0:
        valor = valor - 10
        cont10 += 1
    elif valor % 1 == 0:
        valor = valor - 1
        cont1 += 1

    # Condição de saída do laço - Begin
    if valor == 0:
        break
    # Condição de saída do laço - End

# Processamento de dados - End

# Saída de dados - Begin
print('=' * 50)
if cont100 > 0:
    print(f'A quantidade de notas de 100 é de {cont100}.')
if cont50 > 0:
    print(f'A quantidade de notas de 50 é de {cont50}.')
if cont20 > 0:
    print(f'A quantidade de notas de 20 é de {cont20}.')
if cont10 > 0:
    print(f'A quantidade de notas de 10 é de {cont10}.')
if cont1 > 0:
    print(f'A quantidade de notas de 01 é de {cont1}.')
print('=' * 50)
# Saída de dados - End
