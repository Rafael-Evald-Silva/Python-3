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


# Programa principal
n = leiaint('Digite um valor: ')
print(f'O valor digitado foi {n}')
