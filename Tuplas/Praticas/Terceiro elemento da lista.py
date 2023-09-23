'''Acesse o terceiro elemento da tupla criada no exercício anterior.'''
# Solução Simples e funcional (mas nem tão legal assim :| )
nums = (1, 4, 6, 8, 5)
print(nums,'\nO terceiro elemento da tupla é:',nums[2])

# Solução mais legal :)
from random import randint
nmrs = ()
for n in range(0, 5):
    numeros_aleatorio = randint(0,5)
    nmrs += (numeros_aleatorio, )
print('\n',nmrs)
print('O terceiro elemento da tupla é:',nmrs[2])# type: ignore
