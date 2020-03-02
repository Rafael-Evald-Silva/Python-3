tupla = ('Lápis', 1.75,
         'Borrcha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Cnetas', 22.30,
         'Livro', 34.90)

print('-' * 50)
print(f'{"Lista de preços":^50}')
print('-' * 50)
for c in range(len(tupla)):
    if c % 2 ==0:
        print(f'{tupla[c]:.<30}', end='')
    else:
        print(f'R${tupla[c]:>6.2f}')
print('=' * 50)
