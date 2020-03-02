# Entrada de dados
retas = []
cont = 0
while True:
    reta = float(input(f'Digite o valor da reta {cont+1}: '))
    retas.append(reta)
    cont += 1
    if cont == 3:
        break

# Processamento de dados
if (retas[0] < retas[1] + retas[2]) and (retas[1] < retas[0] + retas[2]) and (retas[2] < retas[0] + retas[1]):
    mensagem = 'Poderá formar um triângulo.'
    if (retas[0] == retas[1]) and (retas[2] == retas[1]):
        tipo = 'EQUILÁTERO'
    elif ((retas[0] == retas[1]) or retas[2] == retas[1]) or (retas[0] == retas[2]):
        tipo = 'ISÓCELES'
    else:
        tipo = 'ESCALENO'
else:
    mensagem = 'Não pode formar um triângulo,'

# Saída de dados
print(f'{mensagem}', end=' ')
if (retas[0] < retas[1] + retas[2]) and (retas[1] < retas[0] + retas[2]) and (retas[2] < retas[0] + retas[1]):
    print(f'do tipo {tipo}.')
