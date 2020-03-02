# Importando bibliotecas
import random

# Variaveis
cont = 0
alunoLista = []

# Entrada de dados
while True:
    aluno = str(input(f'Digite os nomes dos alunos {cont+1}: '))
    alunoLista.append(aluno)
    cont += 1
    if cont == 4:
        break

# Processamento
random.shuffle(alunoLista)

# Saida de dados
print(f'A ordem de apresentação é {alunoLista}.')
