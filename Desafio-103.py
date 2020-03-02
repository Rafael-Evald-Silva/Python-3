def ficha(nome_jogador='0', gols_jogador=0):
    if nome_jogador == '':
        nome_jogador = '<desconhecido>'
    if gols_jogador == 0:
        gols_jogador = 0
    print(f'O {nome_jogador} fez {gols_jogador} no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
