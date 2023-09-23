'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.'''

def verificar(arg):
    print('P' if arg > 0 else 'N')

verificar(float(input('Digite um valor: ')))
