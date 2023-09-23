'''Crie um dicionário com nomes de alunos e suas respectivas médias. Ordene o dicionário por ordem de média (do maior para o menor) e imprima o resultado.'''
from operator import itemgetter

geral = []
ordenar = geral[:]
while True:
    aluno = str(input('Nome: ').strip().capitalize())
    media = float(input('Média: ').strip())
    geral.append({'aluno': aluno, 'media': media})
    while True:
        resp = str(input('\nContinuar? [S/N] ').strip())
        print()
        if resp in 'SsNn':
            break
        print('\nERRO! Escolha S ou N.')
    if resp in 'Nn':
        break

ordenar = sorted(geral, key=itemgetter('media'),reverse=True)

for pos,v in enumerate(ordenar):
    print(v['aluno'], v['media'])
