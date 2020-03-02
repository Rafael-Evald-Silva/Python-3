def voto(ano):
    import datetime
    anoAtual = datetime.date.today().year
    idade = anoAtual - ano
    if idade < 16:
        mensagem = 'NÃO VOTA'
    elif 16 <= idade < 18:
        mensagem = 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        mensagem = 'VOTO OBRIGATORIO'
    else:
        mensagem = 'VOTO OPCIONAL'
    retorno = f'Com {idade} anos: {mensagem}'
    return retorno


anoNascimento = int(input("Qual ano de nascimento? "))
resp = voto(anoNascimento)
print(resp)
