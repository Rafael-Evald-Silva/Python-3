# Iniciando variáveis
valores = list()

# Entrada de dados - Inicio
for c in range(0, 5):
        num = int(input(f'Digite um valor na posição {c}: '))
        valores.append(num)

# Processamento de dados - Inicio
maiorValor = max(valores)
menorValor = min(valores)
# Processamento de dados - Fim

# Saída de dados - Inicio
print(f'{" Analíze dos dados ":=^60}')
print(f'Os valores digitados foram {valores}.')
print(f'O maior valor foi {maiorValor} e foi digitado na posição', end=' ')
for c, v in enumerate(valores):
    if v == maiorValor:
        print(f'{c}, ', end=' ')
print(f'\nO menor valor foi {menorValor} e foi digitado na posição', end=' ')
for c, v in enumerate(valores):
    if v == menorValor:
        print(f'{c}, ', end=' ')
print('\n  ')
print('=' * 60)
# Saída de dados - Fim
