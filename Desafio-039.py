# Entrada de dados
import datetime
anosNascimento = int(input('Informe seu ano de nascimento: '))
anoAtual = datetime.date.today().year
sexo = str(input('Digite o sexo: '))[0]
sexoUpper = sexo.upper()

# Processamento e saída de dados
idade = anoAtual - anosNascimento
print(f'Você possui {idade} anos.')

if sexoUpper == 'F':
    print('Para mulheres o alistamento militar no Brasil, não é obrigatório.')
else:
    if idade == 18:
        print('Hora de se alistar.')
    elif idade < 18:
        print('Ainda vai se alistar.')
        print(f'Seu alistamento foi no ano de {anoAtual + 18}.')
    else:
        print('Já passou do tempo de se alistar.')
        print(f'Ja passou {anoAtual - (idade - 18)} do alistamento.')
