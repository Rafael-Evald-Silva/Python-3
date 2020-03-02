def leiaFloat(num):
    while True:
        try:
            valor = float(input(num))
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
            valor = 0
        except (ValueError, TypeError):
            print('ERRO, favor digite um valor inteiro valido.')
            continue
        else:
            return valor
