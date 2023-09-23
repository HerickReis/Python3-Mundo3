'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário.  No Final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
# Minha resolução
from random import randint
from operator import itemgetter
jogos = {}
lista_sorteados = []

for j in range(1,5):
    sortear = randint(0,10)
    while sortear in lista_sorteados:
        sortear = randint(0,10)
    lista_sorteados.append(sortear)
    jogos[f'Jogador{j}'] = sortear

for jogador in sorted(jogos, key=lambda x: jogos[x], reverse= True):
    print(f'O {jogador} sorteou o número {jogos[jogador]}')

# Resolução da aula
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'Jogador4': randint(1,6)} 
ranking = list() # lista auxiliar 
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tiou {v} no dado')
    sleep(0.6)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # a lista ranking irá receber todos valores do dicionário jogo, porém organizado a partir dos valores da chave 1
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(0.6)
