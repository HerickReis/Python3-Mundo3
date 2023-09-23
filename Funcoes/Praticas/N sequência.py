'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

numeros_inseridos = []
def numeros(numeros_usuario):
    for nums in range(numeros_usuario):
        numeros_inseridos.append(nums + 1)
        for i in numeros_inseridos:
            print("   ".join(str(i)),end=' ')
        print()

numeros(numeros_usuario=int(input('Digite um número: ')))
