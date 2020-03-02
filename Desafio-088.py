# Importando bibliotecas
from random import randint
from time import sleep

# Declarando a lista
jogos = []
copiar = []

# Iniciando variáveis
cont = 1
cont2 = cont3 = 0

# Entrada de dados - Inicio
print(f'{" Jogar na Mega Sena ":=^40}')
jogadas = int(input('Quantos jogos você quer que eu sortei? '))
print('=' * 40)
# Entrada de dados - Fim

# Processamento de dados - Inicio
while cont3 < jogadas:
    while cont2 < 6:
        sorteio = randint(1, 60)
        if sorteio not in copiar:
            copiar.append(sorteio)
            cont2 += 1
    jogos.append(copiar[:])
    copiar.clear()
    cont3 += 1
    cont2 = 0
# Processamento de dados - Fim

# Saída de dados - Inicio
print(f'=-=-=-=-=- Sorteando {jogadas} Jogos -=-=-=-=-=')
for l in range(0, jogadas):
    sleep(1)
    print(f'Jogo {cont}: {sorted(jogos[l])}')
    cont = cont + 1
print('=-=-=-=-=-=-=- Boa Sorte -=-=-=-=-=-=-=')
# Saída de dados - Fim
