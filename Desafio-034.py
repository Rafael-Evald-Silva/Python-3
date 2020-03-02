# Entrada de dados
salario = float(input('Qual o salário do funcionário: R$'))

# Processamento de dados
if salario > 1250:
    novoSalario = ((salario * 0.10) + salario)
else:
    novoSalario = ((salario * 0.15) + salario)

# Saída de dados
print(f'O salário do funcionário após o aumento passa a ser R${novoSalario:.2f}.')
