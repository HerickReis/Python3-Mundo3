# Desafio anterior
'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No Final, mostre a matriz na tela, com a formatação correta.'''
# Atual
'''Aprimore o desafio anterior, mostrando no Final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da tarceira coluna.
C) O maior valor da segunda linha.'''

# MInha resolução
numeros = [[],[],[]]
pares = soma_terceira_coluna = soma_segunda_linha = 0
# "pos" será a posição de cada lista e i é o valor dentro de cada lista.
for pos,i in enumerate(numeros):
    # Irá percorrer cada sublista dentro da lista numeros e irá adicionar 3 valores em cada.
    for sp in range(3):
        adicionar = int(input(f'Digite o valor para [{pos},{sp}] '))
        # Realiza o cálculo dos numeros pares adicionado
        if adicionar % 2 == 0:
            pares += adicionar
        numeros[pos].append(adicionar)
    # Realiza a soma de todos valores no indice 2 (Terceiro valor).
    soma_terceira_coluna += i[2]
# percorre a posição de cada lista.
for sp in range(0,len(numeros)):
    # irá realizar a leitura dos 3 número em cada lista.
    for v in range(3):
        # Irá escrever todos valores de cada lista individualmente deixando-os centralizado nos colchetes [].
        print(f'[{numeros[sp][v]:^3}]',end='')
    # irá adicionar uma quebra de linha a cada iteração.
    print()
print(f'''A soma de todos valores pares é: {pares}.
A soma dos valores da terceira coluna é: {soma_terceira_coluna}.
A soma dos valores na segunda linha é: {max(numeros[1])}.''')# A segunda linha é composta pela segunda lista, então bastou usar o comando max e a 2 lista como argumento.


# Resolução do curso
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linhas in range(0,3):
    for c in range(0,3):
        matriz[linhas][c] = int(input(f'Digite um valor para [{linhas}, {c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ',end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
