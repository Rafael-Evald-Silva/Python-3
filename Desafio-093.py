# Declarado o dicionario e listas e iniciando a variável - inicio
dados = {}
golsPorPartida = []
totalGols = 0   # - fim

# Entrada de dados - inicio
dados['nome'] = str(input('Nome do jogador: '))
qtdPart = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for cont in range(0, qtdPart):
    golsPorPartida.append(int(input(f'Quantos gols na partida {cont}: ')))
dados['gols'] = golsPorPartida[:]
for cont in golsPorPartida:
    totalGols = totalGols + cont
dados['total'] = totalGols  # - fim

# Saída de dados - Inicio
print('-=' * 40)
print(dados)
print('-=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 40)
print(f'O jogador {dados["nome"]} jogou {qtdPart} partidas')
for part, cont in enumerate(golsPorPartida):
    print(f'    => Na partida {part}, fez {cont} gols.')
print(f'Foi um total de {dados["total"]} gols.')  # - Fim
