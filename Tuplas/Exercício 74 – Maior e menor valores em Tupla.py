'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem dos números gerados e também indique o maior e o menor valor que estão na tupla.'''
print('\nMinha resolução\n'.upper())
from random import randint
tupla = ()

for _ in range(5):
    num = randint(0,10)
    tupla += (num, ) # a vírgula serve para que cada valor seja ordenado um na frente do outro a cada iteração do loop

print(f'''Os números gerados são: {tupla}
O maior número foi {max(tupla)}
O menor número foi {min(tupla)}''')


# Resolução do curso
print('\nResolução do curso\n'.upper())
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10),)
print(f'Os valores sorteados foram:',end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')