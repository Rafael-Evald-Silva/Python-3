# Entrada de dados
km = float(input('Quantos KM esse carro percorreu? '))
dias = int(input('Quantos dias o carro foi alugado? '))

# Processamento de dados
preco = ((km*0.15)+(dias*60))

# Saida de dados
print(f'O carro fico alugado por {dias} dias e andou {km} KM cunstado um tonta de R${preco:.2f}')
