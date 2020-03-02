# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip().upper()

# Processamento de dados
procurar = ('SILVA' in nome)
if procurar >= True:
    mesagem = 'Sim'
else:
    mesagem = 'Não'

# Saida de dados
print(f'O nome possui silva? {mesagem}')
