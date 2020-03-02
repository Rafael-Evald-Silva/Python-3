# Entrada de dados
valorMetros = float(input('Digite um valor em metros: '))

# Processamento
valorCentimetros = valorMetros * 100
valorMilimetros = valorMetros * 1000

# Saida de dados
print(f'O valor {valorMetros} convertido para centimetros é {valorCentimetros:.0f}.')
print(f'O valor {valorMetros} convertido para Milimetros é {valorMilimetros:.0f}.')
