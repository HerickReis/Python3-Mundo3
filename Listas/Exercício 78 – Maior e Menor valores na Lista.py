'''Faça um programa que leia 5 valores numéricos a guarde—os em uma lista. 
No final, mostre qual Foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

# Minha Resolução 1
numeros = []
for n in range(5):
    numeros.append(int(input(f'Digite o número para a posição {n}: ')))
menor = min(numeros)
maior = max(numeros)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for cont,mais in enumerate(numeros):
    if mais == maior:
        print(f'{cont}... ',end='')
print(f'\nO menor valor digitado foi {menor} nas posições ',end='')
for cont, mens in enumerate(numeros):
    if mens == menor:
        print(f'{cont}... ',end='')

# Minha resolução 2
numeros_inseridos = []
lista_maior = []
lista_menor = []
for i in range(7):
    numeros_inseridos.append(int(input(f'Digite o {i}º valor: ').strip()))
copia_maior = numeros_inseridos [:]
copia_menor = numeros_inseridos [:]

#Verificar se todas listas estão recebendo parâmetros
#print(f'\nNumeros inseridos {numeros_inseridos}\nCopia Maior {copia_maior}\nCopia menor {copia_menor}\nNumeros Inseridos {numeros_inseridos}\nLista maior {lista_maior}\nLista Menor {lista_menor}')

maior_numero = max(numeros_inseridos)
menor_numero = min(numeros_inseridos)
print(f'''Você digitou os números {numeros_inseridos}
Os maiores números se encontram nas posições: ''',end='') 
for mai in copia_maior:
    procurar = copia_maior.index(maior_numero)
    lista_maior.append(procurar)
    copia_maior[procurar] = 'a'
    print(procurar,end='... ')
    if maior_numero not in copia_maior:
        break
print('\nOs menores números se encontram nas posições: ',end='')
for men in copia_menor:
    procurar = copia_menor.index(menor_numero)
    lista_menor.append(procurar)
    copia_menor[procurar] = 'a'
    print(procurar,end='... ')
    if menor_numero not in copia_menor:
        break

# Resolução da aula

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum} ')
print(f'O menor valor digitado foi {men}nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ',end='')
print()
print(f'O maior valor digitado foi {mai}nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ',end='')
print()
