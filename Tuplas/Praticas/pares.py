'''Crie uma tupla com os números de 1 a 10. Em seguida, crie uma nova tupla contendo apenas os números pares.'''

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = tuple()
for i in numeros:
    if i % 2 == 0:
        pares += (i,)
print(pares) 