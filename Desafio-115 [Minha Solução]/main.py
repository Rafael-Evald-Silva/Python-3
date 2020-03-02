# Importando modulos
import menu
import CadastrarPessoa
import ListaDePessoas
from time import sleep
import colored

while True:
    opc = menu.MenuSelecao()
    if opc == 1:
        ListaDePessoas.ExibindoPessoasCadastradas()
        sleep(3)
    elif opc == 2:
        print(40 * '-')
        print('Novo cadastro'.center(40))
        print(40 * '-')
        import ValidacaoDeDados as leia
        Nome = input('Nome da pessoa: ')
        Idade = leia.leiaInt(input('Idade da pessoa: '))
        CadastrarPessoa.CadastrarPessoa(Nome, Idade)
        sleep(2)
    else:
        break
print(40 * '-')
print('Saindo do sistema, ate logo.'.center(40))
print(40 * '-')
sleep(2)
