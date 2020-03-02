# Entrada de dados
distacia = float(input('Qual a distancia da viagem em KM: '))

# Processamento de dados
if distacia <= 200:
    valor = (distacia * 0.50)
else:
    valor = (distacia * 0.45)

# Saida de dados
mes = ' Resultados '
print(f'{mes:=^35}')
print(f'A viagem é de {distacia} e custará R${valor:.2f}')
