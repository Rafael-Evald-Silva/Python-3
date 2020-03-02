def notas(*n, sit=False):
    """
    -> Faz analise de notas fornecidas mostrado a situação da pessoa.
    :param n: Recebe as notas fornecidas.
    :param sit: Pode ou não mostrar a situação da pessoa em relação a suas notas.
    :return: Retornar um dicionario com as notas e situação da pessoa.
    """

    dados = dict()
    dados['Total'] = len(n)
    dados['Maior Nota'] = max(n)
    dados['Menor Nota'] = min(n)
    dados['Média'] = ((sum(n)) / len(n))
    if sit:
        if dados['Média'] >= 7:
            dados['Situacao'] = 'Boa'
        elif dados['Média'] >= 5:
            dados['Situacao'] = 'Razoavel'
        else:
            dados['Situacao'] = 'Ruim'
    return dados


# Programa principal
resp = notas(5.7, 8, 9, 5, 3, sit=False)
print(resp)
help(notas)
