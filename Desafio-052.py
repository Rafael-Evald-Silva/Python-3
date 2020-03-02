# Entrada de dados
numero = int(input('Digite um número: '))

# Processamento de dados
cont = 0    # Iniciando variável
for c in range(1, numero + 1):
    if numero % c == 0:
        cont += 1

# Saída de dados
if cont < 2:
    print(f'O número {numero} é um número PRIMO.')
else:
    print(f'O número {numero} não é um número PRIMO.')
