def visu():
    print('-' * 40)


def area(ba, alt):
    a = base * altura
    visu()
    print(f'Á area de um terreno {ba}x{alt} é {a}m².')


# Programa principal
print('Controle de terreno')
visu()
base = float(input('Largura(m): '))
altura = float(input('Comprimeito(m): '))
area(base, altura)
