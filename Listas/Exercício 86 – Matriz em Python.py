'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No Final, mostre a matriz na tela, com a formatação correta.'''
# Minha resolução
valores = [[], [], []]
for pos,i in enumerate(valores):
    for a in range(3):
        inserir = int(input(f'Digite um valor para [{pos}, {a}] '))
        valores[pos].append(inserir)
print('-='*30)
for p in range(0,len(valores)):
    for sp in range(3):
        print(f'[{valores[p][sp]:^6}]',end='')
    print()

# Resolução da Aula
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linhas in range(0,3):
    for c in range(0,3):
        matriz[linhas][c] = int(input(f'Digite um valor para [{linhas}, {c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ',end='')
    print()
