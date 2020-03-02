# Entrada de dados
print('{:=^60}'.format(' Lojas Rafael '))
preco = float(input("Informe o preço do produto: R$"))
print('='*60)

# Condição de pagamentos
print('{:=^60}'.format(' Opções de Pagamentos '))
pagamento = int(input('''[ 1 ] Para pagamentos à vista dinheiro/cheque.
[ 2 ] Para pagamentos à vista no cartão.
[ 3 ] Para pagamentos 2x no cartão.
[ 4 ] Para pagamentos 3x ou mais no cartão: '''))
print('='*60)

# Processamento e a saída de dados
print('{:=^60}'.format(' Relatório Final '))
if pagamento == 1:
    print('Para pagamentos a vista o produto recebe 10% de desconto.')
    valor = (preco -(preco * 0.10))
    print(f'O valor do produto era de R${preco:.2f} e passa a ser de R${valor:.2f}.')

elif pagamento == 2:
    print('Para pagamentos a vista no cartão recebe 5% de desconto.')
    valor = (preco - (preco*0.05))
    print(f'O valor do produto era de R${preco:.2f} e passa a ser de R${valor:.2f}.')

elif pagamento == 3:
    print('Para pagamentos em 2x no cartão o preço do produto permanece o mesmo.')
    valor = preco
    print(f'O valor do produto é de R${preco:.2f} e ficará duas parcelas de R${preco/2:.2f} no cartão.')

elif pagamento == 4:
    print('O valor do produto terá um aumento de 20% de juros em 3x ou mais no cartão.')
    valor = ((preco * 0.20) + preco)
    print(f'O valor do produto era de R${preco:.2f} e passa a ser R${valor:.2f}.')
    parcela = int(input('Digite a quantidade de parcelas que deseja parcelar: '))
    print(f'Ficando {parcela} parcelas de R${valor/parcela:.2f}.')
else:
    print('Opção invalida.')
print('='*60)
