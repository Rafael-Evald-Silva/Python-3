# importando bibliotecas
import random

while True:
    # Entrada de dados
    jogoComputador = random.randint(0, 10)
    jogoJogador = int(input('Diga um valor: '))
    while True:
        jogadorEscolha = str(input('Par ou Impar [P/I]: ')).upper()[0]
        if jogadorEscolha in 'PI':
            break

    print('=' * 50)
    # Processamento de dados
    cont = 0    # Iniciando variável cont
    if jogadorEscolha == 'P':

        if (jogoComputador + jogoJogador) % 2 == 0:
            jogo = 'PAR'
            cont += 1
            print('Parabéns você venceu.')
            print(f'Você jogo {jogoJogador} e computador jogo {jogoComputador}.')
            print(f'Total deu {jogoJogador+jogoComputador} e deu {jogo}; ')
        else:
            jogo = 'IMPAR'
            print('GAME OVER.')
            print(f'Você jogo {jogoJogador} e computador jogo {jogoComputador}.')
            print(f'Total deu {jogoJogador+jogoComputador} e deu {jogo}; ')
            break
    else:
        if (jogoJogador + jogoComputador) % 2 == 1:
            jogo = 'IMPAR'
            cont += 1
            print('Parabéns você venceu.')
            print(f'Você jogo {jogoJogador} e computador jogo {jogoComputador}.')
            print(f'Total deu {jogoJogador+jogoComputador} e deu {jogo}; ')
        else:
            jogo = 'PAR'
            print('GAME OVER.')
            print(f'Você jogo {jogoJogador} e computador jogo {jogoComputador}.')
            print(f'Total deu {jogoJogador+jogoComputador} e deu {jogo}; ')
            break
    print('=' * 50)

# Saída de dados
print(f'Jogo FINALIZADO, você conseguiu {cont} vitorias consecutivas.')
