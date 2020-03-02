# Entrada de dados
num = int(input('Digite um valor inteiro qualquer: '))

# Processamento
if num % 2 == 0:
    mensagem = 'PAR'
else:
    mensagem = 'IMPAR'

# Saida de dados
saida = ' Resultado '
print(f'{saida:=^35}')
print(f'O número digita é {mensagem}.')
