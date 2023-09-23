'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
lista = [4, 12, 8, 27, 19, 33, 55, 10, 7, 21, 16, 92, 1, 11, 6, 30, 14, 5, 23, 17]
par = []
impar = []
for n in lista:
    if n % 2 == 0:
        par.append(n)
    if n % 2 >0:
        impar.append(n)

print(f'''Os pares são: {par}
e os impares são: {impar}''')