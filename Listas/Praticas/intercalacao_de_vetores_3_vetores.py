# Primeira forma
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
intercalados = lista1 + lista2 + lista3
print(intercalados)

# Segunda forma
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
intercalado = []

for i in lista1:
    intercalado.append(i)
for i2 in lista2:
    intercalado.append(i2)
for i3 in lista3:
    intercalado.append(i3)
print(intercalado)
