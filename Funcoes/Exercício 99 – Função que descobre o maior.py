'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
'''from time import sleep
def maior(*nums):
    numero_maior = 0
    print('-=' * 50)
    for analise in nums:
        sleep(0.4)
        print(analise,end=' ',flush=True)

    print(f'Foram informados {len(nums)} valores ao todo.')
    
    # Forma com a função max()
    # print(f'O maior valor informado foi {max(nums)}' if len(nums) > 0 else f'O maior valor informado foi 0')

    # Forma sem max()
    for n in nums:
        if n > numero_maior:
            numero_maior = n
    print(f'O maior valor informado foi {numero_maior}' if len(nums) > 0 else f'O maior valor informado foi 0')
# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(3 ,5 ,1 ,0)
maior(4, 6, 7)
maior(0, -4)
maior()'''

# Resolução do curso
from time import sleep

def maior(* núm):
    cont = maior = 0
    print('\nAnalisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(3 ,5 ,1 ,0)
maior(4, 6, 7)
maior(0, -4)
maior()
