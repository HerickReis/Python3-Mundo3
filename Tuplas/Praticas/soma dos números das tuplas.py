'''Escreva um programa que receba duas tuplas de números e retorne uma nova tupla contendo a soma dos elementos correspondentes de cada tupla.'''
tupla_1 = (4, 5, 6, 7)
tupla_2 = (1, 3, 5, 7, 9)
resultado = ()
total = total2 = 0
for t in tupla_1:
    total += t
for tot in tupla_2:
    total2 += tot
resultado += (total, total2)
busca = resultado.index(total)
busca2 = resultado.index(total2)
print(f'O resultado da 1º tupla é: {resultado[busca]}\nO resultado da 2º tupla é: {resultado[busca2]}')