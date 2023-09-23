'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No Final, mostre um boletim contando a média da cada um e permita que o usuário possa mostrar as notas da cada aluno individualmente.'''
# Minha Resolução
from time import sleep
geral = []
while True:
    total = 0
    dado = []
    notas = []

    nome = str(input('Nome: ').strip().capitalize())
    dado.append(nome)

    for n in range(2):
        nota = float(input(f'Nota {n+1}: '))
        notas.append(nota)
        total += nota
    media = total / len(notas)

    dado.append(notas[:])
    dado.append(media)

    geral.append(dado)
    r = str(input('\nQuer coninuar? [S/N] ').strip()[0])
    print('-='*30)
    print()
    while r not in 'SsNn':
        print('Resposta inválida!')
        sleep(0.3)
        r = str(input('\nQuer coninuar? [S/N] ').strip()[0])
        print('-='*30)
        print()
    if r in 'Nn':
        break

print(f'''{'No.'}{'Nome':>6}{'Média':>13}''')
print('--'*30)

for pos,i in enumerate(geral):
        print(f'''{pos}{i[0]:>10}{i[2]:>10.1f}''')
print('--'*25)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (-1 interrompe): ')) # Achei melhor colocar -1 ao invés de 999
    print('~~'*20)
    print(f'\nNotas de {geral[aluno][0]} são {geral[aluno][1]}\n')
    print('~~'*20)
    if aluno == -1:
        print('FINALIZANDO...')
        sleep(0.4)
        break
print('<<< Volte Sempre >>>')

# Resolução do curso
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('Finalizando...')
        break
if opc <= len(ficha) -1:
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
