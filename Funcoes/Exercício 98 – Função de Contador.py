'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e realize o passo da contagam.
Seu programa tem que realizar três contagens através da Função criada:
a) De 1 até 10. de 1 em 1
B) De 10 até O. de 2 em 2
c)Uma contagem personalizada.'''
'''from time import sleep

def contador(inicio, fim, passo):
    if passo == 0 :
        print('\nO passo não pode ser 0, então vou considerar 1\n')
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}' if passo >= 0 else f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}')

    # Fará uma contagem crescente
    if inicio < fim:
        for contagem in range(inicio, fim + 1, passo):
            sleep(0.3)
            print(contagem,end=' ',flush=True)

    # Fará uma contagem decressente, caso o passo for maior que 0
    elif inicio > fim and passo > 0:
        for contagem in range(inicio, fim - 1, - passo):
            sleep(0.3)
            print(contagem,end=' ',flush=True)

    # Fará a contagem decressiva
    elif passo < 0:
        for contagem in range(inicio, fim - 1, passo):
            sleep(0.3)
            print(contagem, end=' ',flush=True)


# Programa principal
    print('FIM!')
    print()

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de decidir a contagem!\n')
contador(inicio = int(input('Inicio: ')), fim = int(input('Fim: ')), passo = int(input('Passo: ')))'''


# Resolução do curso
from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1

    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
