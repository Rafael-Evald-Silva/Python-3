# Importando bibliotecas
from random import randint

# Entrada de dados
computador = randint(0, 10)

# Entrada de dados
varControle = ''
cont = 0
while varControle != 'S':
    print('O computador penso em um número entre 0 a 10.')
    jogador = int(input('Qual número você acha que computador penso? '))

    # Processamento de dados
    cont += 1
    # Dicas pro jogador
    if jogador < computador:
        print('Mais... Tente novamente.')
    else:
        print('Menos... Tente novamente..')

    # Condição de saída do laço
    if jogador == computador:
        varControle = 'S'

# Saída de dados
print(f'O computador penso no número {computador} e você preciso de {cont} para acerta o número.')
