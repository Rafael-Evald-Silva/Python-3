def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço, retornado o resutado com ou sem formatção.
    :param preco: Valor em dinheiro.
    :param taxa: Porcetagem que sera aumentado.
    :param formato: Mostrar os dados formatado com forma de dinheiro.
    :return: Retorna o resutado do aumento.
    """
    resp = ((preco * taxa) / 100)
    return resp if formato is False else moeda(resp)


def diminuir(preco=0, taxa=0, formato=False):
    resp = ((preco * taxa) / 100)
    resp = preco - resp
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    resp = preco * 2
    return resp if not formato else moeda(resp)


def metade(preco=0, formato=False):
    resp = (preco /2)
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaMim=10, taxaMax=5):
    print('-' * 50)
    print('Resumo do Valor'.center(50))
    print('-' * 50)
    print(f'O dobro do de {preco} é \t\t{dobro(preco, True)}.')
    print(f'A metade de {preco} é \t\t{metade(preco, True)}.')
    print(f'Com acrecimo de {taxaMax}% fica \t{aumentar(preco, taxaMax, True)}.')
    print(f'Com desconto de {taxaMim}% fica \t{diminuir(preco, taxaMim, True)}.')
    print('-' * 50)
