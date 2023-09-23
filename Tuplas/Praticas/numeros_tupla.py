'''Crie uma tupla chamada numeros com cinco números inteiros de sua escolha. Imprima a tupla.'''
numeros = (1, 3, 5, 7, 9)
numeros_formatados = ' '.join(str(n) for n in numeros)# formatar os numeros da lista é necessarios transformalos em string pois o método ' '.join funciona apenas com strings
print(numeros_formatados)