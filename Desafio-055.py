# Entrada de dados
cont = 0
maiorPeso = 0
menorPeso = 0
for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))

    # Processamento de dados
    cont += 1
    if cont == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

# Saída de dados
print(f'Dos pesos digitados o maior foi {maiorPeso}Kg e  menor foi {menorPeso}Kg.')
