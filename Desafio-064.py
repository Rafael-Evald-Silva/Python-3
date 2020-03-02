# Entrada de dados
numero = cont = soma = 0  # Iniciando as variável

# Entrada de dados
numero = int(input('Digite um número inteiro [999 para parar]: '))
while numero != 999: # Inicio do laço de repetição
    cont += 1
    soma = soma + numero
    numero = int(input('Digite um número inteiro [999 para parar]: '))  # Fim do laço

# Saída de dados
print(f'Foi digitado {cont} números e a soma entre todos eles foi {soma}.')
