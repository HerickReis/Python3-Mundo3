'''Crie uma função que receba uma tupla de valores e retorne a média aritmética desses valores.'''

valores = (1, 1, 2, 3, 5, 8, 13, 21)
total = 0
for a in valores:
    total += a

print(f'\nO total dos valores na tupla é {total} e a média é de: {total / len(valores)}\n')