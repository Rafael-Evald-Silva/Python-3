def aumentar(preco, taxa):
    resp = ((preco * taxa) / 100)
    return resp


def diminuir(preco, taxa):
    resp = ((preco * taxa) / 100)
    resp = preco - resp
    return resp


def dobro(preco):
    resp = preco * 2
    return resp


def metade(preco):
    resp = (preco /2)
    return resp
