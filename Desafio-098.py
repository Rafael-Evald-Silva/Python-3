# Importando biblioteca - {Inicio
from time import sleep


# Funções - {Inicio
def contador(ini, fi, pas):
    print('-=' * 20)
    if ini < fi:
        print(f'Contagem de {ini} ate {fi} de {pas} em {pas}.')
        for c in range(ini, fi + 1, pas):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('Fim')
    else:
        print(f'Contagem de {ini} ate {fi} de {pas} em {pas}.')
        for c in range(ini, fi - 1, -pas):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('Fim')


# Programa principal - {Inicio
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo < 0:
    passo = passo * -1
if passo == 0:
    passo = 1
contador(inicio, fim, passo)
