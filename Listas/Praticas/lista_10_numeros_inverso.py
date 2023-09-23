'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fim = len(lista) - 1
# 1 forma
'''print('1 Forma')
lista.sort(reverse=True)
print(lista)'''

# 2 forma
'''print('\n2 Forma')
print(lista[::-1])'''

# 3 forma
print('\n3 Forma')

for i in range(len(lista)//2):
    aux = lista[i]
    lista[i] = lista[fim]
    lista[fim] = aux
    fim -= 1

print(lista)
