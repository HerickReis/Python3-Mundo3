'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números Foram digitados.

B) lista de valores, ordenada da Forma decrescente.

C) Se o valor 5 Foi digitado e está ou não na lista.'''


## Minha Resolução Sem sorted()
numeros = []

while True:
    numeros_inserido = int(input('Informe um número inteiro: ').strip())
    if len(numeros) == 0:
        numeros.append(numeros_inserido)
    else:
        for indice in range(0,len(numeros)):
            if numeros_inserido >= numeros[indice]:
                numeros.insert(indice,numeros_inserido)
                break
        else:
            numeros.append(numeros_inserido)
    resposta = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if resposta == 'N':
        break
print(f'''Foram digitados {len(numeros)} números.
Os valores em ordem decrescente são: {numeros} ''')
print(f'O valor 5 está na posição {numeros.index(5)} lista' if 5 in numeros else '5 não está na lista')

# Com sorted()
nums = []
while True:
    numeros_usuario = int(input('Informe um número inteiro: ').strip())
    nums.append(numeros_usuario)
    r = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    if r == 'N':
        break
nums.sort(reverse=True)
print(f'''Foram digitados {len(nums)} números.
Os valores em ordem decrescente são: {nums} ''')
print(f'O valor 5 está na posição {nums.index(5)} lista' if 5 in nums else '5 não está na lista')


# Resolução da aula
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')