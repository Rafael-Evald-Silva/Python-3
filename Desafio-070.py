# Iniciando as variáveis
totalGasto = prodMaisMil = prodMaisBarato = cont = 0
nomeProdMaisBar = ''

while True:     # Inicio do laço de repetição infinito
    # Entrada de dados - Begin
    print('=' * 50)
    nomeProd = str(input('Nome do Produto: '))
    precoProd = float(input('Preço do Produto: R$'))
    # Entrada de dados - End

    # Processamento de dados - Begin
    totalGasto += precoProd
    if precoProd > 1000:
        prodMaisMil += 1
    cont += 1
    if cont == 1:
        prodMaisBarato = precoProd
        nomeProdMaisBar = nomeProd
    else:
        if precoProd < prodMaisBarato:
            prodMaisBarato = precoProd
            nomeProdMaisBar = nomeProd
    # Processamento de dados - Begin

    # Artificio de saída do laço - Begin
    while True:    # Inicio da validação de dados
        saida = str(input('Deseja continuar? [S/N]')).upper()[0]
        if saida in 'SN':
            break   # Fim da validação de dados
    if saida == 'N':
        break   # Fim do laço de repetição infinito
    # Artificio de saída do laço - End

# Saída de dados - Begin
print('=' * 50)
print(f'O total da compra foi de R${totalGasto:.2f}.')
print(f'No total foram comprado {prodMaisMil} produtos com valor superior a 1000 reais.')
print(f'O produto mais barato foi {nomeProdMaisBar} e custo R${prodMaisBarato:.2f}.')
# Saída de dados - End
