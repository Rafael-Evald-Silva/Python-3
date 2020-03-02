# Importando biblioteca
import datetime

# Declarando dicionario
dados = dict()

# Entrada de dados
dados['Nome'] = input('Nome: ')
dataNas = int(input('Ano de nascimento: '))
dados['Idade'] = (datetime.date.today().year - dataNas)
dados['CTPS'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if dados['CTPS'] > 0:
    dados['Ano contratação'] = int(input('Ano de contratação (0 caso nunca tenha sido contratado): '))
    if dados['Ano contratação'] > 0:
        dados['Salario'] = float(input('Salário: '))
        anosContr = (35 - (datetime.date.today().year - dados['Ano contratação']))
        if anosContr > 0:
            dados['Aposentadoria'] = anosContr + dados['Idade']
        else:
            dados['Aposentadoria'] = dados['Idade'] + anosContr

# Saída de dados
print('-=' * 20)
for k, v in dados.items():
    print(f'{k} tem valor {v}.')
