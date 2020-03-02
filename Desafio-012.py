# Entrada de dados
precoProdu = float(input('Digite o preço do produto: R$'))

# Processamento de dados
novoPreco = (precoProdu - (precoProdu * 0.05))

# Saida de dados
print(f'O preço do produto era de R${precoProdu:.2f} e com desconto de 5% passa a ser R${novoPreco:.2f}.')
