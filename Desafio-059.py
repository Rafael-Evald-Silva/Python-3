# Importado bibliotecas
from time import sleep

# Iniciação das variáveis
varControle = ''
valores = []
cont = 0

# Entrada de dados com for
entradaDados = ' Entrada de dados '
print(f'{entradaDados:=^40}')
for c in range(1, 3):
    valore = int(input(f'Digite valor {c}: '))
    valores.append(valore)
print('=' * 40)

while varControle != 'S':
    if cont == 0:
        # Opção de ação
        menu = ' Menu de Seleção '
        print(f'{menu:=^40}')
        varControle = int(input('''
        Escolha uma opção:
        [1] Somar os valores.
        [2] Multiplicar os valores.
        [3] Maior valor.
        [4] Novos valores.
        [5] Sair do programa.
        Digite a opção: '''))
        print('='*40)
    else:
        sleep(3)
        # Opção de ação
        menu = ' Menu de Seleção '
        print(f'{menu:=^40}')
        varControle = int(input('''
        Escolha uma opção:
        [1] Somar os valores.
        [2] Multiplicar os valores.
        [3] Maior valor.
        [4] Novos valores.
        [5] Sair do programa.
        Digite a opção: '''))
        print('=' * 40)
    cont += 1

    # Processamento de dados
    if varControle == 1:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        soma = valores[0] + valores[1]
        # Saída de dados
        print(f'A soma dos valores {valores[0]} e {valores[1]} é {soma}')
        print('=' * 40)

    elif varControle == 2:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        multiplicacao = valores[0] * valores[1]
        # Saída de dados
        print(f'A multiplicação dos valores {valores[0]} e {valores[1]} é {multiplicacao}.')
        print('=' * 40)

    elif varControle == 3:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        # Saída de dados
        if valores[0] > valores[1]:
            print(f'O maior valor e {valores[0]}')
        else:
            print(f'O maior valor é {valores[1]}')
        print('=' * 40)

    elif varControle == 4:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        # Entrada de dados com for
        for c in range(1, 3):
            valore = int(input(f'Digite valor {c}: '))
            valores.append(valore)
        print('=' * 40)

    # variável de controle de saída do laço
    elif varControle == 5:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        varControle = 's'
        if varControle in 'Ss':
            varControle = str(input('Deseja mesmo sair? ')).upper()[0]
        print('=' * 40)

    else:
        resultado = ' Resultado '
        print(f'{resultado:=^40}')
        print('Opção digitada invalida, favor digite uma opção valida.')
        print('=' * 40)

# Saída de dados
print('=' * 40)
print('Fim da aplicação.')
print('=' * 40)
