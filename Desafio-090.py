# Iniciando dicionario
dados = dict()

# Entrada de dados
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'A média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'

# Saída de dados
print(f'Nome é igual a {dados["nome"]}.')
print(f'A média é {dados["media"]}.')
print(f'A situação de {dados["nome"]} é {dados["situação"]}.')
