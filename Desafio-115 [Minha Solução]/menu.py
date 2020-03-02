def MenuSelecao():
    print(40 * '-')
    print('Menu de Seleção'.center(40))
    print(40 * '-')
    print('01 - Ver pessoas cadastradas.')
    print('02 - Cadastrar uma nova pessoa.')
    print('03 - Sair do sistema.')
    print(40 * '-')
    while True:
        try:
            opc = int(input('Sua opção: '))
            if opc > 3:
                print('Erro, favor digite um valor valido.')
            else:
                break
        except (TypeError, ValueError):
            print('Erro, favor digite um valor valido.')
    return opc
