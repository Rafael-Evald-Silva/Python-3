# Entrada de dados
import datetime

anoAtual = datetime.date.today().year
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))

# Processamento de dados
idade = anoAtual - anoNascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

# Saída de dados
print(f'A categoria do atleta é {categoria}.')
