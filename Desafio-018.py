# OBS não rodo verificar na correção porque não rodo

# Importando bibliotecas
import math

# Entrada de dados
angulo = int(input('Digite um angulo qualquer: '))

# Processamento
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

# Saida de dados
print('===' * 10)
print(f'O seno do angulo {angulo} é {seno:.2f}.')
print(f'O cosceno do angulo {angulo} é {cos:.2f}')
print(f'A tangente do angulo {angulo} é {tan:.2f}')
print('===' * 10)
