'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''
notas_alunos = []
bimestres = 4
cont = 0
for n in range(10):
    notas_totais = 0
    print('_'*40)
    print(f'{n+1}º ALUNO')
    print('_'*40)
    for b in range(bimestres):
        notas = float(input(f'\nDigite a nota do {b+1}º bimestre: '))
        notas_totais += notas
    print(f'\nMédia: {notas_totais / bimestres}\n')
    notas_alunos.append(notas_totais / bimestres)
    
for na in notas_alunos:
    if na >= 7.0:
        cont += 1
if cont == 0:
    print(f'Nenhum aluno obteve a média igual ou superiror a 7.0')
else:
    print(f'Houveram {cont} alunos com média igual ou maior a 7.0 .' if cont > 1  else f'Houve {cont} aluno com média igual ou maior a 7.0 .')