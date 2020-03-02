# Entrada de dados
salario = float(input('Digite o valor do salario: R$'))

# Processamento de dados
novoSalario = ((salario * 0.15) + salario)

# Saida de dados
print(f'O salario do funcionario era de R${salario:.2f} e passa a ser de R${novoSalario:.2f} com 15% de aumento.')
