def leiaDinheiro(dinheiro):
    ok = False
    valor = 0
    while True:
        n = str(input(dinheiro)).replace(',', '.').strip()
        if n.isalpha() or n== '':
            print(f'O valor {n} digitado não e valor valido.')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return valor


def leiaint(mes):
    ok = False
    valor = 0
    while True:
        n = str(input(mes))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Valor digitado não é numerico, favor digite um valor numerico.')
        if ok:
            break
    return valor
