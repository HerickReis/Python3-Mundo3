'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No Final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.'''
# Minha Resolução
'''pessoas = list()
informacoes = list()
mais_leve = mais_pesada = tot = 0
while True:
    tot += 1
    informacoes.append(str(input('\nNome: ').strip().capitalize()))
    informacoes.append(float(input('Peso: ').strip()))
    pessoas.append(informacoes[:])
    informacoes.clear()
    resposta = str(input('\nQuer continuar? [S/N] ').strip()[0])
    while resposta not in 'SsNn':
        resposta = str(input('\nQuer continuar? [S/N] ').strip()[0])
    if resposta in 'Nn':
        break

for cont,p in enumerate(pessoas):
    if cont == 0:
        mais_pesada = mais_leve = p[1]
    else:
        if p[1] < mais_leve:
            mais_leve = p[1]
        elif p[1] > mais_pesada:
            mais_pesada = p[1]
print('-=' * 20)
print(f'Foram cadastradas ao todo {tot} pessoas')
print(f'\nO maior peso registrado foi {mais_pesada}Kg. peso de ',end='')
for pes in pessoas:
    if pes[1] == mais_pesada:
        print(f'[{pes[0]}]',end=' ')
print(f'O menor peso registrado foi {mais_leve}Kg. peso de ',end='')
for lev in pessoas:
    if lev[1] == mais_leve:
        print(f'[{lev[0]}]',end=' ')'''

# Resolução da aula
temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi de {mai} kg. peso de',end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso for de {men}Kg.',end='')
for p in principal :
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
