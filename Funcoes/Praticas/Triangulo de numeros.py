'''Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.'''

def formatado(numero_usuário):
    if numero_usuário == 0:
        print('0')
    for n in range(0, numero_usuário):
            print(f'{n + 1} ' * (n + 1))


formatado(numero_usuário=int(input('Digite um número inteiro: ')))
