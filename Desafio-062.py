# Entrada de dados
primeiroTermo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

# Processamento de dados
termo = primeiroTermo
cont = 1
vaControle = 10
total = 0
vaControle = 10
while vaControle != 0:
    total = total + vaControle
    while cont <= total:
        print(f'{termo} -> ', end='')
        cont = cont + 1
        termo = termo + razao
    vaControle = int(input('\nQuantos termos a mais você quer mostrar? '))

# Saída de dados
print(f'Progressão finalizada com {total} mostrado.')

# Não consegui fazer sozinho.
