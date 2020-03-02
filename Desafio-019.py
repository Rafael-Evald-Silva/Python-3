# Importando bibliotecas
import random

# Variaveis
cont = 0 # Contador
lista = [] # Vetor ou lista

# Entrada de dados
while True:
    aluno = str(input('Digite o nome do aluno: '))
    lista.append(aluno) # Adiciona a variavel ao vetor
    cont += 1
    if cont == 4:
        break

# Processamento
aluSorteado = random.choice(lista)

# Saida de dados
print(f'O aluno sorteado foi {aluSorteado}.')
