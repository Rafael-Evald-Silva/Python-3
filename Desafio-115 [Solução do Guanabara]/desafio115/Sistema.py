from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)

while(True):
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # Ver pessoas cadastradas
        LerArquivo(arq)
    elif resp == 2:
        # Cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome da pessoa: '))
        idade = leiaInt('Idade da pessoa: ')

        Cadastrar(arq, nome, idade)
    elif resp == 3:
        # Sair do sistema
        print('Saíndo do sistema, até logo...')
        break
    else:
        print('Erro, digite uma opção valida.')
    sleep(2)
