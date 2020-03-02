# Entrada de dados
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Entrada de dados -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
valorCasa = float(input('Informe o valor da casa: R$'))
valorSalario = float(input('Informe o seu salário: '))
anosPagamento = int(input('Informe quantos anos irar pagar: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# Processamento de dados
print('=-=-=-=-=-=-=-=-=-=-=-=-=--=-= Saída de dados -=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
prestacao = (valorCasa / (anosPagamento * 12))
print(f'Para pagar uma casa de R${valorCasa:.2f} em {anosPagamento} anos.', end=' ')
print(f'a prestação sera de R${prestacao:.2f}.')

if (valorSalario * 0.30) >= prestacao:
    print('Parabéns, seu empréstimo foi APROVADO.')
else:
    print('Sinto muito mas seu salário é incompatível com imóvel que senhor deseja comprar.')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
