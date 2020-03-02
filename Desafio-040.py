# Entrada de dados
notas = []
cont = 0
while True:
    nota = float(input(f'Digite a nota {cont+1}: '))
    notas.append(nota)
    cont += 1
    if cont == 2:
        break

# Processamento e saída de dados
media = (notas[0] + notas[1]) / 2
print(f'Sua primeira nota é {notas[0]} e sua segunda nota é {notas[1]}, sua media foi {media:.2f}.')
if media < 5.0:
    print('Aluno retido.')
elif (media >= 5.0) and (media < 6.9):
    print('Aluno de RECUPERAÇÃO.')
else:
    print('Aluno APROVADO.')
