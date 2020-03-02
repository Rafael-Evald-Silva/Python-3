# Importado bibliotecas - {Inicio
from time import sleep


# Funções - {Inicio
def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os dados...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
    print(f'Foram informado {len(num)} valores.')
    print(f'O maior valor é {maior}')


# Programa principal - {Inicio
maior(1, 3, 4, 5, 6)
maior(3, 5, 7)
maior(1, 3)
maior(1)
maior()
