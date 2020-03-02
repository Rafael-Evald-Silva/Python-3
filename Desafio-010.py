# Entrada de dados
valorReais = float(input('Quanto de dinheiro você possui? '))

# Processamento
valorDolares = valorReais / 3.27

# Saida de dados
print(f'Você tem R${valorReais} e pode comrpar US${valorDolares:.2f}.')
