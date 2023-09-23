'''Faça um programa que tenha uma lista chamada números e duas Funções chamadas Sorteia() e somaPar(). A primeira Função vai sortear números e vai colocá—los dentro da lista e a
segunda Função vai mostrar a soma entre todos os valoras PARES sorteados pela Função anterior.'''
from random import randint
from time import sleep

'''def sorteia():
    print(f'Sorteando 10 valores da lista: ',end='')
    for _ in range(10):
        nums_sorteados = randint(0,10)
        numeros.append(nums_sorteados)
        print(f'\033[32m{nums_sorteados}\033[m',end=' ',flush=True)
        sleep(0.4)
    print('Pronto\n')

sorteia()
def somapar(numeros_lista):
    soma = 0
    print(f'Somando todos valores pares de \033[33m{numeros}\033[m, ',end='')
    for nums in numeros_lista:
        if nums % 2 == 0:
            soma += nums
    print(f'temos {soma}')

numeros = []
somapar(numeros)'''

# Resolução do curso
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteado 5 valores da lista: ',end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)   # A lista números está sendo passada como argumento para a função, toda modificação dentro do argumento terá efeito em ambas.
        print(f'{n} ',end='',flush=True)
        sleep(0.3)
    print('Pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os vlaores pares de {lista},temos {soma}.')


números = list()
sorteia(números)
somapar(números)
