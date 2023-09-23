'''Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, respectivamente, 
escreva um programa que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média.'''

primeira_prova = (5, 9, 10, 7, 8)
segunda_prova = (7, 6, 10, 10, 9)
tot1 = tot2 = 0
print(f'As notas da turma na prova 1 foi de: ',end='')
for i1, pn in enumerate(primeira_prova): # i2 é o contador do laço, ele conta quantas repetições foram feitas dentro do loop, 
#o enumerate na tupla serve para enumerar cada elemento assim transformando cada elemento da tupla em listas
    tot1 += pn
    if i1 < len(primeira_prova) -1: # o len irá contar a quantidade de elementos presentes, o -1 será para descartar o último número, isso irá acontecer até o contador do laço for maior ou igual a quantidade de elementos presentes na tupla
        print(pn, end=', ') # após tudo isso o end = ', ' irá organizar todos elementos em uma única linha 
    else:
        print(pn) # se o contador do laço i1 for maior ou igual a quantidade de elementos da tupla o ultimo elemento será exibido sem vírgula após ele

print(f'\nAs notas da turma na prova 2 foi de: ',end='')
for i2, sn in enumerate(segunda_prova):
    tot2 += sn
    if i2 < len(segunda_prova) -1 :
        print(sn,end=', ')
    else:
        print(sn)

media1 = tot1 / len(primeira_prova)
media2 = tot2 / len(segunda_prova)
print()
print(f'A turma tirou a melhor nota na prova 1' if media1 > media2 else 'A turma tirou a melhor nota na prova 2')