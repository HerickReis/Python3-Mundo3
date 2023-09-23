'''Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''
# Primeira forma
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

intercalados = lista1 + lista2
print(intercalados)

# Segunda forma
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
intercalado = []

for i in lista1:
    intercalado.append(i)
for i2 in lista2:
    intercalado.append(i2)
print(intercalado)
