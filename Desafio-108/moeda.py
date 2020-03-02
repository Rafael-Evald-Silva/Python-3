def aumentar(preco=0, taxa=0):
    resp = ((preco * taxa) / 100)
    return resp


def diminuir(preco=0, taxa=0):
    resp = ((preco * taxa) / 100)
    resp = preco - resp
    return resp


def dobro(preco=0):
    resp = preco * 2
    return resp


def metade(preco=0):
    resp = (preco /2)
    return resp


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
