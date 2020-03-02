# Entrada de dados
varControle = ' '
sexo = str(input('Informe o sexo [F/M] ')).upper()[0]
while sexo not in 'MmFf':   # while usado pra validar dados
    print('Dados inválidos, ', end=' ')
    sexo = str(input('Informe o sexo [F/M] ')).upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
