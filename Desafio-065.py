# Iniciando as variáveis
varControle = ''
soma = somaDosValores = menorValor = maiorValor = cont = 0

# Entrada de dados
while varControle != 'N':
    varControle = 'S'
    if varControle == 'S':
        numeros = int(input('Digite um número: '))

        # Processamento de dados
        if cont == 0:
            menorValor = numeros
            maiorValor = numeros
        else:
            if menorValor > numeros:
                menorValor = numeros
            else:
                maiorValor = numeros
        cont += 1
        soma += numeros

    # Opção de controle do laço
    varControle = str(input('Deseja continuar? ')).upper()[0]

# Processamento de dados
media = soma / cont

# Saída de dados
print(f'Você digito {cont} valores e a media dos valores é {media}.')
print(f'O menor valor digitado foi {menorValor}.')
print(f'O maior valor digitado foi {maiorValor}.')
