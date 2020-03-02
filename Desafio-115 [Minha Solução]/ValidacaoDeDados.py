def leiaFloat(num):
    while True:
        try:
            valor = float((num))
        except KeyboardInterrupt:
            print('O usuario preferiu interromper a aplicação.')
            return 0
        except (ValueError, TypeError):
            print('ERRO, favor digite um valor float valido.')
            continue
        else:
            return valor


def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
        except KeyboardInterrupt:
            print('O usuario preferiu interromper a aplicação.')
        except (ValueError, TypeError):
            print('ERRO, favor digite um valor valido.')
            continue
        else:
            return valor
