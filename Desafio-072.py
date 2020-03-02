# Entrada de dados - Inicio
numTupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Desoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num >= 0 and num <= 20:
        break
    else:
        num = int(input('Tente novamente, Digite um número entre 0 e 20: '))
# Entrada de dados - Fim

# Saída de dados - Inicio
print(f'Você digito o número {numTupla[num]}.')
# Saída de dados - Fim
