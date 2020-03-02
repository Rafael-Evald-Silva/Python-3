# Declarando listas
dados = []

while True:
    # Entrada de dados
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    # Processamento de dados
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])

    # Saída do laço
    varControle = str(input('Deseja cadastrar mais? [S/N]')).upper()[0]
    if varControle in 'N':
        break

# Saída de dados
print('=' * 40)
print(f'{"No":<4} {"Nome":<10} {"Média":>8}')
for i, n in enumerate(dados):
    print(f'{i:<4} {n[0]:<10} {n[2]:>8.1f}')

while True:
    # Entrada de dados - Para escolher a nota de quem sera exibido
    print('=' * 40)
    opc = int(input('Deseja mostrar a nota de qual aluno? [999 para interromper] '))

    # Saída do laço infinito
    if opc == 999:
        print('Finalizado...')
        break

    # Saída de dados - Mostrar o nome e nota do aluno
    if opc <= len(dados) - 1:
        print('-' * 40)
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
