# Entrada de dados
frase = str(input('Digite uma frase: ')).strip().upper()

# Processamento de dados
letraA = frase.count('A')
letraA1 = (frase.find('A')+1)
letraA2 = (frase.rfind('A')+1)

# Saida de dados
print(f'Na frase a letra A aparece {letraA} vezes.')
print(f'A primeria vez que a letra A apareceu foi na posição {letraA1}')
print(f'A ultima vez que a letra A apareceu foi na posição {letraA2}.')
