'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.'''
numeros = [3, 6, 9 , 12, 18, 24, 52, 42, 35, 10]
soma = 0
print(f'Os números originais são: {numeros}')
for cont,q in enumerate(numeros):
    quadrado = q ** 2
    numeros[cont] = quadrado
    soma += quadrado
print(f'''Os quadrados de todos numeros são : {numeros}
A soma de todos é: {soma}''')