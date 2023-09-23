'''Crie uma função que receba uma tupla de palavras e retorne uma nova tupla contendo o número de caracteres de cada palavra.'''

palavras = ('Abacaxi', 'Frutinha', 'Suco', 'Manhã', 'Chuva', 'Sol', 'Quente', 'Frio', 'Seco', 'Molhado')
for p in palavras:
    print(f'A palavra {p} possui {len(p)} caracteres')