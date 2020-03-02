soma = 0  # Variáveis iniciada
cont = 0  # Variáveis iniciada
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma dos {cont} valores e o números {soma}.')
