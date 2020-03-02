# Entrada de dados
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# Processamento de dados
imc = (peso / (altura * altura))
if imc < 18.5:
    mensagem = 'ABAIXO DO PESO'
elif 18.5 <= imc <= 25:
    mensagem = 'PESO IDEAL'
elif 25 <= imc < 30:
    mensagem = 'SOBREPESO'
elif 30 <= imc < 40:
    mensagem = 'OBESIDADE'
else:
    mensagem = 'OBESIDADE MÓRBIDA'

# Saída de dados
print(f'O seu IMC é de {imc:.2f} e você esta {mensagem}.')
