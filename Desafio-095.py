# Declarado o dicionario e listas e iniciando a variável - inicio
dados = {}
time = []
golsPorPartida = []
totalGols = 0   # - fim
while True:
    # Entrada de dados - inicio
    dados['nome'] = str(input('Nome do jogador: '))
    qtdPart = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    golsPorPartida.clear()
    for cont in range(0, qtdPart):
        golsPorPartida.append(int(input(f'Quantos gols na partida {cont}: ')))
    dados['gols'] = golsPorPartida[:]
    for cont in golsPorPartida:
        totalGols = totalGols + cont
    dados['total'] = totalGols
    time.append(dados.copy())   # - fim

    # Saída do laço infinito - Inicio
    while True:
        varContr = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if varContr in 'SN':
            break
        print('Erro! Favor digite apenas S ou N.')
    if varContr in 'N':
        break   # - Fim

# Saída de dados - Inicio
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}' ,end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo {busca}.')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i} fez {g} gols.')
    print('-=' * 30)
print('Fim da aplicação')
