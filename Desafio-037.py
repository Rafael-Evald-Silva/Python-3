# Entrada de dados
numero = int(input('Digite um valor qualquer: '))

# Processamento de dados
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

selecao = int(input("""[ 1 ] Para Binario.
[ 2 ] Para Hexadecimal
[ 3 ] Para Octal

Faça sua escolha: """))

if selecao == 1:
    print(f'O numero {numero} em Binário é {binario[2:]}.')
elif selecao == 2:
    print(f'O número {numero} em Hexadecimal é {hexadecimal[2:]}.')
elif selecao == 3:
    print(f'O número {numero} em Octal é {octal[2:]}.')
else:
    print('Opção invalida.')
