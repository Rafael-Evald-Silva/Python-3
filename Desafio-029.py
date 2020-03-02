# Entrada de dados
veloCarro = float(input('Digite a velocidade do carro: '))

# Processamento de dados
if veloCarro > 80:
    mesangem = 'Você foi multado.'
    multa = (f'A multa sera de R${((veloCarro - 80) * 7):.2f}.')
else:
    mesangem = 'Parabens você esta dentro do limite de velocidade.'

# Saida de dados.
print(f'{mesangem}')
if veloCarro > 80:
    print(f'{multa}')
