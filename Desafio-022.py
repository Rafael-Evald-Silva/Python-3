# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip()

# Processamento
nomeMaisculo = nome.upper()
nomeMinusculos = nome.lower()
qtdLetras = len(nome) - nome.count(' ')
qtdLetrasPrimeiro = nome.find(' ')
nomeSplitado = nome.split()

# Saida de dados
print(f'O nome em maisculo é {nomeMaisculo}.')
print(f'O nome em minusculo é {nomeMinusculos}.')
print(f'O nome tem {qtdLetras} letras.')
print(f'O primeiro nome tem {qtdLetrasPrimeiro} letras.')
print(f'Seu primeiro nome é {nomeSplitado[0]} e tem {len(nomeSplitado[0])}')
