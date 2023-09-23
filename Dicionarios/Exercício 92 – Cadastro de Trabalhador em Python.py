'''Crie um programa que leia nome, ano de nascimento a carteira de trabalho e cadastra—os (com idade) em um dicionáriose por acaso a CTPS For diferente de ZERO,
o dicionário raceberá também o ano da contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
# Minha Resolução
from datetime import datetime

infos_gerais = {}
tempo_contribuicao = 35

nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
carteira_de_trabalho = int(input('Carteira de trabalho (0 não tem): '))

data_atual = datetime.now()
hoje = data_atual.year
idade = hoje - nascimento

infos_gerais['nome'] = nome
infos_gerais['nascimento'] = nascimento
infos_gerais['ctps'] = carteira_de_trabalho
infos_gerais['idade'] = idade

if carteira_de_trabalho > 0:
    ano_contratacao = int(input('Ano de contratação: '))
    salário = float(input('Salário: '))

    tempo_trabalhado = 35 - (hoje - ano_contratacao) + idade

    infos_gerais['ano_contratacao'] = ano_contratacao
    infos_gerais['salario'] = salário
    infos_gerais['aposentadoria'] = tempo_trabalhado

print('-='*30)
print(f'Nome: {infos_gerais["nome"]}')
print(f'Idade: {infos_gerais["idade"]}')
print(f'CTPS: {infos_gerais["ctps"]}' if infos_gerais["ctps"] > 0 else 'Não possui CTPS.')

if carteira_de_trabalho != 0:
    print(f'\nContratação: {infos_gerais["ano_contratacao"]}')
    print(f'Salário: {infos_gerais["salario"]}')
    print(f'Aposentadoria: {infos_gerais["aposentadoria"]}')

# Resolução do curso
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário : R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
