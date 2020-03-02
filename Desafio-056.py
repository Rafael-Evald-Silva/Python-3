# Variáveis
mediaIdade = 0
maiorIdadeHomem = 0
qtdMulheres = 0
nomeHomemMaisVelho = ' '

# Entrada de dados
for c in range(0, 4):
    print('{:=^40}'.format(' Entrada de dados '))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [F/M]'))
    sexoUpper = sexo.upper()[0]
    print('='*40)

    # Processamento de dados
    mediaIdade += idade
    if idade > maiorIdadeHomem:
        maiorIdade = idade
        if sexoUpper == 'M':
            nomeHomemMaisVelho = nome
    if idade < 20:
        if sexoUpper == 'F':
            qtdMulheres += 1

# Processamento de dados fora do laço
mediaIdade = (mediaIdade / 4)

# Saída de dados
print('{:=^40}'.format(' Resultados '))
print(f'A media de idade do grupo é {mediaIdade}.')
print(f'O nome do homem mais velho é {nomeHomemMaisVelho}.')
print(f'No total {qtdMulheres} tem menos de 20 anos.')
print('=' * 40)
