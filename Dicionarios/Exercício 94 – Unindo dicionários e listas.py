'''Crie um programa que leia nome, sexo e idade de várias pessoas, quardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No Final, mostre:
A) Quantas pessoas foram cadastradas

B) A média de idade do grupo.

c) Uma lista com todas as mulheres.

D) Uma lista com todas as pessoas com idade acima da média.'''
# Minha resolução
from time import sleep

infos_gerais = []
total_idade = mulheres = acima_media = 0

print('''\n\033[34mOlá, bem vindo ao sitema de cadastros, aqui você poderá cadastrar várias pessoas, 
para interromper e exibir todas pessoas cadastradas basta não inserir o nome e pressionar Enter.\033[m''')
sleep(1)

while True:
    nome = str(input('\nNome: ').strip().capitalize())
    if not nome:
        break
    sexo = str(input('Sexo (Masculino [M] / Feminino[F]):  ').strip()[0])
    while sexo not in 'MmFf':
        print('\n\033[1;31mSexo inválido, por favor insira uma informação válida.\033[m')
        sexo = str(input('\n\tSexo (Masculino [M] / Feminino[F]):  ').strip()[0])

    idade = int(input('Idade: '))
    total_idade += idade
    print('-' * 60)

    infos_gerais.append({'nome': nome, 'idade':idade, 'sexo': sexo})

print('-=' * 30)
print(f'- Ao todo foram cadastradas {len(infos_gerais)} pessoas')
print(f'- A média de idade do grupo é de: {total_idade / len(infos_gerais):.0f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')

for pos, sex in enumerate(infos_gerais):
    if sex['sexo'] in 'Ff':
        mulheres += 1
        print(sex['nome'],end=' ')
if mulheres == 0:
    print('\033[1;33mNenhuma mulher cadastrada.\033[m')
            
print('\n\n- A lista das pessoas com idade acima da média são: ')

for k, v in enumerate(infos_gerais):
    if infos_gerais[k]['idade'] > total_idade / len(infos_gerais):
        print(f'\nnome = {infos_gerais[k]["nome"]}; sexo = {infos_gerais[k]["sexo"]}; idade = {infos_gerais[k]["idade"]}')
        acima_media += 1
if acima_media == 0:
    print('\033[1;33mNão há pessoas com idade acima da média.\033[m')


# Resolução do curso
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: [M/F] ').upper())
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]').upper()[0])
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f}')
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO')