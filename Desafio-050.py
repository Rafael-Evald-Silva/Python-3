# Iniciando variável
soma = 0
cont = 0

# Entrada de dados
for c in range(1,7):
    numero = int(input(f'Digite um número {c}: '))

    # Processamento de dados
    if numero % 2 == 0:
        soma += numero  # Acumulador
        cont += 1   # Contador

# Saída de dados
print(f'A soma dos {cont} números pares e a soma foi {soma}.')
