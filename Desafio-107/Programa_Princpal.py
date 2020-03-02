import Moedas

# Entrada de dados
p = float(input('Digite um valor? '))

# Sída de dados
print(f'A metade de {p} é {Moedas.metade(p)}.')
print(f'O dobro de {p} é {Moedas.dobro(p)}.')
print(f'Aumentado 10%, em {p} temos {Moedas.aumentar(p, 10)}.')
print(f'Diminuindo 13%, em {p} temos {Moedas.diminuir(p, 13)}.')
