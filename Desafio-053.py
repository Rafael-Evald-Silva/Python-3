# entrada e dados
frase = str(input('Digite uma frase: '))

# Tratamento da frase
fraseUpper = frase.upper().strip().split()
junto = ''.join(fraseUpper)

# Variáveis
inverso = ''

# Processamento de dados
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    resultado = 'TEMOS UM PALÍNDROMO'
else:
    resultado = 'NÃO TEMOS UM PALÍNDROMO'

# Saída de dados
print(f'Frase digitada {junto}, Frase inversa {inverso}.', end='')
print(f' e {resultado}.')
