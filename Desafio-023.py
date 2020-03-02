# Entrada de dados
numero = int(input('Digite um valor entre 0 e 9999: '))

# Processamento de dados
unidade = (numero // 1 % 10)
dezena = (numero // 10 % 10)
centena = (numero // 100 % 10)
milhar = (numero // 1000 % 10)

# Saida de dados
print(f'Analizando o numero {numero}')
print(f'Unidade é {unidade}.')
print(f'Dezena é  {dezena}.')
print(f'Centena é {centena}.')
print(f'Milhar é  {milhar}.')
