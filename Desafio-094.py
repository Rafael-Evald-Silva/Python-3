# Declarando dicionario e lista - Inicio
dados = {}
dadosGeral = []  # - Fim

# Iniciando variável somadora - Inicio
somaIdade = 0  # - Fim

# Entrada de dados - Inicio
while True:
    dados.clear()
    print('-=' * 30)
    dados['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
        if sexo in 'MF':
            break
        print('Erro, por favor digite apenas M ou F.')
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    somaIdade = somaIdade + dados['idade']
    dadosGeral.append(dados.copy())  # - Fim

    # Condição de saída do laço infinito - Inicio
    print('--' * 30)
    while True:
        varContro = str(input('Deseja continuar[N/S]: ')).upper()[0]
        if varContro in 'SN':
            break
        print('ERRO! Por favor digite apenas Sim ou Não.')
    if varContro in 'N':
        break  # - Fim

# Processamento de dados - Inicio
mediaIdade = somaIdade / len(dadosGeral)  # - Fim

# Saída de dados - Inicio
print('-=' * 30)
print(f'-a) Foram cadastrados no total {len(dadosGeral)} pessoas.')
print(f'-b) A média de idade do grupo é {mediaIdade:.2f} anos.')
print(f'-c) As mulheres cadastradas foram ', end='')
for cont in dadosGeral:
    for k, v in cont.items():
        if k == 'sexo' and v == 'F':
            print(f'{cont["nome"]}', end=' ')
print(f'\n-d) Lista de pessoas que estão com idade acima da média.')
for cont in dadosGeral:
    if cont['idade'] > mediaIdade:
        print(f'        Nome = {cont["nome"]}; sexo = {cont["sexo"]}; idade = {cont["idade"]}')
print('<< Encerrado >>')  # - Fim
