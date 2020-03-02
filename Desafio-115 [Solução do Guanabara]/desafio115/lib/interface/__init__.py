def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
        except KeyboardInterrupt:
            print('O usuario preferiu interromper a aplicação.')
            valor = 0
        except (ValueError, TypeError):
            print('ERRO, favor digite um valor inteiro valido.')
            continue
        else:
            return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
