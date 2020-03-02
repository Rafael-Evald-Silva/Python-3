import moeda

# Entrada de dados
p = float(input('Digite um valor? '))

# Sída de dados
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentado 10%, em {moeda.moeda(p)} temos {moeda.aumentar(p, 10, True)}.')
print(f'Diminuindo 13%, em {moeda.moeda(p)} temos {moeda.diminuir(p, 13, True)}.')
