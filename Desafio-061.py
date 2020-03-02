# Entrada de dados
prinmeiroTermo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

# Processamento de dados
termo = prinmeiroTermo
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    cont += 1
    termo = termo + razao

# Saída de dados
print('FIm')

# OBS: não consegui fazer sozinho.
