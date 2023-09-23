'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No Final, mostre o conteúdo da estrutura na tela.'''
# Minha resolução
alunos = {}

nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
alunos['nome'] = nome
alunos['media'] = media
if media >= 7.0:
    alunos['situacao'] = 'Aprovado'
else:
    alunos['situacao'] = 'Reprovado'
print('=-' * 30)
print(f'{alunos["nome"]} tem média {alunos["media"]} e a situação é {alunos["situacao"]}')

# Resolução do curso

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] >= 7: # Método que sempre esqueço, verifica se um número esta entre x valor e y valor, em certas situações é melhor que o range() principalmente em numeros float()
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k,v in aluno.items():
    print(f' - {k} é igual a {v}')
