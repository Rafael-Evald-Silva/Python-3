# Importando bibliotecas
import math

# Entrada de dados
catOP = float(input('Digite o cateto oposto: '))
catAD = float(input('Digite o cateto adjacente: '))

# Processamento de dados
hipot = math.hypot(catOP, catAD)
hipot2 = (catOP ** 2 + catAD ** 2) ** (1/2)

# Saida de dados
print(f'A hipotenusa do triangulo é {hipot:.2f}')
print(f'A hipotenusa do triangulo é {hipot2:.2f}')

