# Entrada de dados
cidadeNome = str(input('Digite o nome da cidade: ')).strip().upper()

# Processamento de dados
cidade = cidadeNome.split()
if cidade[0] == 'SANTO':
    mensagem = 'Sim'
else:
    mensagem = 'Não'
    
# Sainda de dados
print(f'A sitade começa com santo {mensagem} ')
