# Iniciação das variáveis - begin
contMaior = contHomensCad = contMulheresMenosDeVinte = 0

while True:
    # Entrada de dados - begin
    print('=' * 50)
    idade = int(input('Digite idade da pessoa: '))
    while True:
        sexo = str(input('Digite o sexo da pessoa [M/F]:')).upper()[0]
        if sexo in 'MF':
            break

    while True:
        varControle = str(input('Deseja continuar? [S/N]')).upper()[0]
        if varControle in 'NS':
            break
    # Entrada de dados - end

    # Processamento de dados - begin
    if sexo in 'Mm':
        contHomensCad += 1
    if idade > 18:
        contMaior += 1
    if sexo == 'F' and idade < 20:
        contMulheresMenosDeVinte += 1
    # Processamento de dados - end

    # Variável de controle do laço - begin
    if varControle in 'Nn':
        break
    # Variável de controle do laço - end

# Saída de dados - begin
print('=' * 50)
print(f'No total foram cadastrados {contHomensCad} homens foram cadastrados.')
print(f'No total foram cadastrados {contMaior} pessoas maior de 18 anos.')
print(f'No total foram cadastrados {contMulheresMenosDeVinte} mulheres com menos de 20 anos.')
# Saída de dados - end
