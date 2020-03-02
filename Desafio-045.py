# Importando bibliotecas
import random
from time import sleep

# Entrada de dados
print('{:=^40}'.format(' Jokenpô '))
intens = ('PEDRA', 'PAPEL', 'TESOURA')
jogadaComputador = random.randint(0, 2)
jogadaJogador = int(input('''Faça sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA: '''))

print('=' * 40)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
# Processamento
if jogadaComputador == 0:  # Pedra
    if jogadaJogador == 0:
        jogada = 'EMPATE'
    elif jogadaJogador == 1:
        jogada = 'VITORIA'
    elif jogadaJogador == 2:
        jogada = 'DERROTA'
    else:
        print('Jogada invalida.')

elif jogadaComputador == 1:  # Papel
    if jogadaJogador == 0:
        jogada = 'DERROTA'
    elif jogadaJogador == 1:
        jogada = 'EMPATE'
    elif jogadaJogador == 2:
        jogada = 'VITORIA'
    else:
        print('Jogada invalida.')

elif jogadaComputador == 2:  # Tesoura
    if jogadaJogador == 0:
        jogada = 'VITORIA'
    elif jogadaJogador == 1:
        jogada = 'DERROTA'
    elif jogadaJogador == 2:
        jogada = 'EMPATE'
    else:
        print('Jogada invalida.')

# Saída de dados
print('{:=^40}'.format(' Resultado '))
print(f'Você jogo {intens[jogadaJogador]}.')
print(f'O computador jogo {intens[jogadaComputador]}.')
print('-'*40)
print(f'Você obteve {jogada}.')
print('='*40)
