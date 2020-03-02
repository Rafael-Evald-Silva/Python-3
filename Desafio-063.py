# Entrada de dados
print('=' * 40)
print('Sequência de Fibonacci')
print('=' * 40)
n = int(input('Quantos termos você que mostrar? '))
# Processamento de dados
t1 = 0
t2 = 1
# Saída de dados
print('-' * 40)
print(f'{t1} -> {t2}', end='')
# Processamento de dados
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> Fim')


# Não consegui fazer sozinho. -_-
