# Importando bibliotecas
from random import randint

# Entrada de dados - Inicio
num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
# Entrada de dados - Fim

# Processamento de dados - Inicio
menorValor = maiorValor = cont = 0
for c in num:
    if cont == 0:
        menorValor = c
        maiorValor = c
    else:
        if menorValor > c:
            menorValor = c
        if maiorValor < c:
            maiorValor = c
    cont = cont + 1
# Processamento de dados - Fim

# Saída de dados - Inicio
print(f'Os números gerdos foram {num}.')
print(f'O menor valor foi {menorValor}.')
print(f'O maior valor foi {maiorValor}.')
# Saída de dados  Fim
