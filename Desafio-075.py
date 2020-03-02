# Entrada de dados - Inicio
num = int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um vlor: ')), int(input('Digite o ultimo valor: '))
# Entrada de dados - Fim

# Processamento de dados - Inicio
cont3 = cont = 0
valorPar1 = valorPar2 = valorPar3 = valorPar4 = 0
for c in num:
    if c == 3:
        cont3 += 1
    if c % 2 == 0 and cont == 0:
        valorPar1 = c
    if c % 2 == 0 and cont == 1:
        valorPar2 = c
    if c % 2 == 0 and cont == 2:
        valorPar3 = c
    if c % 2 == 0 and cont == 3:
        valorPar4 = c
    cont += 1
valorPar = valorPar1, valorPar2, valorPar3, valorPar4
# Processamento de dados - Fim

# Saída de dados - Inicio
print(f'Os valores digitados foram {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if cont3 >= 1:
    print(f'O primeiro valor 3 apareceu na posição {num.index(3) +1 }.')
else:
    print('O valor 3 não foi digitado nem uma vez.')
print(f'Os valores pares digitaos foram', end=' ')
for c in valorPar:
    if c > 0:
        print(c, end=' ')
# Saída de dads - Fim
