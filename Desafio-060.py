# Entrada de dados
numero = int(input('Digite um valor qualquer: '))

# Iniciando variáveis
cont = numero    # Contador
fat = 1     # Iniciando variável fat

# Processamento de dados
print(f'O fatorial {numero}!', end='')
while cont >= 1:
    fat = fat * cont
    cont -= 1

# Saída de dados
print(f' = {fat}.')
