import utilidadesCeV.moeda as moeda
import utilidadesCeV.dado as dado

# Entrada de dados
b = dado.leiaDinheiro('Digite um valor em dinheiro R$')
moeda.resumo(b, 40, 10)
