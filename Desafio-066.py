# Iniciando as variável
cont = soma = 0

# Corpo do programa
while True:
    # Entrada de dados
    numero = int(input('Digite um valor [999 para para]: '))
    # Condição de saída
    if numero == 999:
        break
    # Processamento de dados
    cont = cont + 1
    soma = soma + numero
# Saída de dados
print(f'Foram digitado {cont} números e a soma entre ees foram de {soma}.')
