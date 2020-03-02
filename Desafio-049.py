# Entrada de dados
numero = int(input('Digite o número que deseja ver a tabuada: '))

# Processamento de dados
mes = f' Tabuada do {numero} '
print(f'{mes:=^40}')
for c in range(1, 11):
    print(f'{numero} x {c:2} = {numero * c:2}')
print('='*40)
