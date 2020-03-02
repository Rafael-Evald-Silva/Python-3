# Iniciando as variáveis
pilha = list()

# Entrada de dados
exp = str(input('Digite a expreção: '))


# Processamento de dados
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

# Saída de dados
if len(pilha) == 0:
    print('Essa expreção aritmetica é valida.')
else:
    print('Essa expreção aritmetica não é valida.')
