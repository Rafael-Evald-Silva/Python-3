# Variaveis
retas = []
cont = 0

# Entrada ded ados
while True:
    reta = float(input(f'Digite a reta {cont+1}: '))
    retas.append(reta)
    cont += 1
    if cont == 3:
        break
if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[1] + retas[0]:
    mensagem = 'Sim, pode formar um triangulo'
else:
    mensagem = 'Não, não pode formar um triangulo'

# Saida de dados
print(f'As retas {retas[0]}, {retas[1]} e {retas[2]} pode ou não formar um trnagulo ? {mensagem}.')
