def ExibindoPessoasCadastradas():
    print(40 * '-')
    print('Pessoas Cadastradas'.center(40))
    print(40 * '-')

    arq_dados = open('dados.txt', 'r')
    print(f'{"NOME":<34}{"IDADE":^6}')
    print(40 * '-')
    for linha in arq_dados.readlines():
        dados = linha.split()

        nome = ' '.join(dados[:-1])
        idade = dados[-1]

        print(f'{nome:<34} {idade:<5}')
    print(40 * '-')
    arq_dados.close()
