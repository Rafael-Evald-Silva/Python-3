# Importando bibliotecas
from random import randint
from time import sleep

# Entrada de dados
computador = randint(0,5) # Faz o computador sortear um valor entre 0 e 5.
print('=-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar.....')
print('=-=-' * 20)
jogador = int(input('Que número eu pensei? ')) # O jogador tenta adivinhar.

# Processamento de dados
print('PROCESSANDO...')
sleep(1) # Criar um delei de um segundo.
if jogador == computador:
    mensagem = 'PARABÉNS, você conseguiu vencer.'
else:
    mensagem = (f'PERDEU, eu pensei no {computador} e você no {jogador} mais sorte na proxima.')

# Saida de dados
print(f'{mensagem}')
