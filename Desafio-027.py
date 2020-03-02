# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip().split()

# Processamento de dados
primeiroNome = nome[0]
cont = len(nome)
ultimoNome = nome[cont - 1]

# Saida de dados
print(f'O primeiro nome da pessoa é {primeiroNome}')
print(f'O ultimo nome da pessoa é {ultimoNome}l.')
