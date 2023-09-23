'''Crie uma lista de números repetidos e, em seguida, conte quantas vezes cada número aparece. Armazene os resultados em um dicionário.'''
from operator import itemgetter
lista_numeros = [1, 1, 1, 5, 2, 7, 5, 2, 7, 9, 10, 1, 4, 6, 4, 2, 7, 8, 9]
resultado = {}
organizado = {}
for nums in lista_numeros:
    contador = lista_numeros.count(nums)
    if nums not in resultado:
        resultado[f'{nums}'] = contador

organizado = sorted(resultado.items(), key=itemgetter(1), reverse=True)

for k,v in organizado:
    print(f'{k:<5}: {v:<3}')
