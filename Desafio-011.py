# Entrada de dados
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

# Processamento
area = largura * altura
qtTintas = area / 2

# Saida de dados
print(f'A area da parede é de {area} metros quadrados')
print(f'Sera necessario {qtTintas} latas de tintas para pitar a parede.')
