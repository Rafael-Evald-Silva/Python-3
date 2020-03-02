tupla = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlêtico Mineiro', 'Goías', 'Botafogo', 'Bahia', 'São Paulo', 'Corinthians',
         'Grêmio', 'Athletic-PR', 'Ceará', 'Fortaleza', 'Vasco da Gama', 'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')

# Processamento de dados - Inicio
cont = chapPosi = 0
for c in tupla:
    if c == 'Chapecoense':
        chapPosi = cont+1
    cont = cont + 1
# Processamento de dados - FIm

# Saída de dados - Inicio
print(f'Os cincos primeiros colocados são {tupla[:5]}.')
print(f'Os quatros ultimos colocas são {tupla[-4:]}.')
print(f'Os nomes dos times na ordem alfabetica é {sorted(tupla)}.')
print(f'A Chapecoence esta na posição {chapPosi}.')
# Saída de dados - Fim
