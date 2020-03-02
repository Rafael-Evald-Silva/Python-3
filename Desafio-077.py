palavras = ('arroz', 'feijao', 'carne', 'frango',
           'mandioca', 'tempero', 'canarao', 'bife',
           'pizza', 'cartao')

for c in palavras:
    print(f'\nNa palavra {c} temos as vogais', end='-> ')
    for letra in c:
        if letra.lower() in 'aeiuo':
            print(letra, end=' ')
