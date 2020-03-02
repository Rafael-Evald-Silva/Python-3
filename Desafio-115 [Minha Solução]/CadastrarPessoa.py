def CadastrarPessoa(nome, idade):
    id = str(idade)
    try:
        arg_dados = open('dados.txt', 'r')
        cont_nome = arg_dados.readlines()
        cont_idade = arg_dados.readlines()
        cont_Linha1 = arg_dados.readlines()   #Para quebrar linhas
        cont_Linha2 = arg_dados.readlines()     # Para quebrar linhas
        cont_nome.append(nome)
        cont_Linha1.append(' ') # Para quebrar linhas
        cont_idade.append(id)
        cont_Linha2.append('\n')

        arg_dados = open('dados.txt', 'w')
        arg_dados.writelines(cont_nome)
        arg_dados.writelines(cont_Linha1)   #   Para quebrar linhas
        arg_dados.writelines(cont_idade)
        arg_dados.writelines(cont_Linha2)   # Para quebrar linhas
        arg_dados.close()

        print(f'Registro de {nome}, cadastrada com sucesso.')
    except FileNotFoundError:
        arg_dados = open('dados.txt', 'w', encoding='utf-8')
        arg_dados.close()
        print('O arquivo não existia e foi criado com sucesso.')
