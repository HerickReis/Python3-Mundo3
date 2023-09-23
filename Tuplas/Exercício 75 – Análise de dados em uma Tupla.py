'''Desenvolva um programa que leia quatro valores pelo teclado e guarde—os em uma tupla. 
No Final,
mostre:
A) Quantas vezas apareceu o valor 9.
B) Em que posição foi digitadoo primeiro valor 3.
C) Quais foram os números pares.'''
print('\nMinha resolução\n'.upper())
tupla = ()
pares = ()
for _ in range(1,5):
    valores = int(input(f'Digite um numero: '))

    if valores % 2 == 0:
        pares += (valores, )
    tupla += (valores,)

nove = tupla.count(9)
print('\nO número 9 não foi inserido' if nove == 0 else f'O valor 9 apareceu {nove} vez/es')

tres = tupla.index(3) if 3 in tupla else None
print(f'O primerio valor 3 apareceu na {tres+1}° posição' if tres is not None else 'O valor 3 não foi inserido' )

print(f'Os valores pares são {pares}')

# Resolução da aula
print('\nResolução do curso\n'.upper())
núm = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')),
    )
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi inserido em nenhuma posição')
print('Os valores pares digitado foram', end=' ')
for n in núm:
    if n % 2 == 0 :
        print(n, end=' ')