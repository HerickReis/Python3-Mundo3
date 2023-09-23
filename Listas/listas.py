'''num = [2, 5 ,9 ,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Esta lista tem {len(num)} elementos')'''

'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

'''a = [2, 3, 4, 7]
b = a[:] # Todos valores de a irão para b, desta forma irá ser feita uma cópia, sem o [:] terá uma ligação
b[2] = 8
print(f'O número 4 está na posição {a.index(4)}')
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Ao igualar uma lista a outra, o python faz uma ligação entre elas, assim toda modificação que ocorrer em uma irá ocorrer na outra.'''

