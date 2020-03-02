def fatorial(num, show=False):
    """
    -> Função para mostrar o fatorial de um valor:
        :param num: Recebe o número a ser fatorado.
        :param show: Mostrar o processo de fatoramento ou não.
        :return: Retorna o resultado do fatorial
    """
    fat = num
    cont = num
    if show:
        print(f'{num}', end=' x ')
    while True:
        cont -= 1
        if show:
            print(f'{cont}', end=' x ')
        fat *= cont
        if cont == 1:
            break
    return fat


numero = int(input('Digite o número a ser fatorado: '))
mostrar = bool(input('Deseja mostrar o processo de fatoramento? [True/False]'))
ren = fatorial(numero, mostrar)
print(f'{ren}')
