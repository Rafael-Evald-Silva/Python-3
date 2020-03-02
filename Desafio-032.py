# Importando bibliotecas
from datetime import date

# Entrada de dados
ano = int(input('Que ano quer analisar, coloque 0 para analizer o ano atual: '))

# Processamento de dados
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    mensagem = 'é Bissesto.'
else:
    mensagem = 'não e Bissesto.'

# Saida de dados
print(f'O ano {ano}  {mensagem}')
