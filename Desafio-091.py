# Importando biblioteca
from random import randint
from time import sleep
from operator import itemgetter

# Declarando dicionario
jogadores = {}

# Declarando uma lista
rank = []

# Entrada de dados
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

# Saída de dados
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tiro {v}.')
    sleep(1)

# Processamento de dados
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Saída de dados
print('-=' * 30)
print('A classificação foi:')
for i, v in enumerate(rank):
    print(f'    {i+1}º lugar {v[0]} com {v[1]}.')
    sleep(1)
