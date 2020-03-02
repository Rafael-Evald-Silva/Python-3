# Corpo do programa
while True:
    # Entrada de dados
    numero = int(input('Digite o numero que deseja ver a tabuada: '))
    # Para sair finalizar a aplicação {
    if numero < 0:
        break
    # }
    # Iniciando variável cont {
    cont = 1
    # }
    # Processamento de dados {
    visual = f'========= Tabuada do {numero} ========='
    print(f'{visual}')
    while True:
        print(f'{numero} x {cont:2} = {cont * numero:2}')
        if cont == 10:
            break
        cont = cont + 1
    print('=' * 40)
    # }
# Fim da aplicação
print('Aplicação finalizada.')
