# Importando biblioteca - Inicio{
from random import randint
from time import sleep      #}

# Declarando lista - Inicio{
num = list()


# Funções - # Inicio
def sorteia(lst):
    print('Sorteando 5 valores', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        num.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('Pronto.')


sorteia(num)


def somaPar(n):
    soma = 0
    print('Os valores par são', end=' ')
    for c in num:
        if c % 2 == 0:
            print(f'{c}', end=' ')
            soma = soma + c
    print(f'e a Soma dos valores par foi {soma}')


somaPar(num)
