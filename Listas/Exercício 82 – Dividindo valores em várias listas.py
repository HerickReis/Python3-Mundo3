'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente.
No Final, mostre o conteúdo das três listas geradas.'''
# Minha Resolução com um loop for dentro do loop while
numeros = []
pares = []
impares = []
while True:
    numeros_usuario = int(input('Digite um número inteiro: '))
    numeros.append(numeros_usuario)
    r = str(input('Deseja continuar ? [S/N] ').upper().strip()[0])
    while r not in 'SN':
        r = str(input('Deseja continuar ? [S/N] ').upper().strip()[0])
    if r == 'N':
        for n in numeros:
            if n % 2 == 0:
                pares.append(n)
            else:
                impares.append(n)
        break
print('-='*50)
print(f'''A lista completa é {numeros}
A lista de pares é {pares}
A lista de impares é {impares}\n''')

# Minha resolução com três loops 
numeros = []
pares = []
impares = []
while True:
    numeros_usuario = int(input('Digite um número inteiro: '))
    numeros.append(numeros_usuario)
    r = str(input('Deseja continuar ? [S/N] ').upper().strip()[0])
    while r not in 'SN':
        r = str(input('Deseja continuar ? [S/N] ').upper().strip()[0])
    if r == 'N':
        for n in numeros:
            if n % 2 == 0:
                pares.append(n)
            else:
                impares.append(n)
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
for i in numeros:
    if i % 2 > 0:
        impares.append(i)
print('-='*50)
print(f'''A lista completa é {numeros}
A lista de pares é {pares}
A lista de impares é {impares}\n''')

# Resolução da aula
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é : {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é {ímpares}')