# Importando bibliotecas
import datetime

# Entrada de dados
anoAtual = datetime.date.today().year   # Para pegar o ano atual
contMaiorIdade = 0  # Inicia a variável
contMenorIdade = 0  # Inicia a variável
for c in range(1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento {c}: '))

    # Processamento de dados
    idade = anoAtual - anoNascimento
    if idade <= 21:
        contMenorIdade += 1
    else:
        contMaiorIdade += 1

# Saída de dados
print(f'Das idades digitadas {contMenorIdade} são menor de idade.')
print(f'Das idades digitadas {contMaiorIdade} são maior de idade.')
