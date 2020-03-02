# Entrada de dados
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
descimo = (primeiroTermo + (10 - 1) * razao)

# Processamento de dados
for c in range(primeiroTermo, descimo + razao, razao):
    print(f'{c}', end='-> ')
print('Acabou')
