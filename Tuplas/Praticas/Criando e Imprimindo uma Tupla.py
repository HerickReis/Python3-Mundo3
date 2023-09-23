'''Crie uma tupla com os números de 1 a 5 e imprima-a.'''
# Solução Simples e funcional (mas nem tão legal assim :| )
nums = (1, 4, 6, 8, 5)
print(nums)

# Solução mais legal :)
from random import randint
nmrs = ()

for n in range(5):
    numeros_aleatorio = randint(0,5)
    nmrs += (numeros_aleatorio, ) # este método nao adiciona valores as tuplas pois elas são imutáveis, ele apenas cria um outra tupla que conterá os valores originais e os novos :)

print(nmrs)

