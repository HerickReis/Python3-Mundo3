'''Crie um programa que gerencie o aproveitamento de um jogador da futebol.  O programa vai ler o nome do jogador quantas partidas ele jogou. 
Depois vai ler a quantidade de gols Feitos em cada partida partida.  
No Final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
# Minha Resolução 
infos_jogador = {}
gols = []
total = 0
nome_jogador = str(input('Nome do jogador: ').strip().capitalize())
infos_jogador['nome'] = nome_jogador
qntd_partidas = int(input(f'\nQuantas partidas {nome_jogador} jogou ? ').strip())

for p in range(qntd_partidas):
    qntd_gols = int(input(f'Quantos gols na {p + 1}ª partida? '))
    total += qntd_gols
    gols.append(qntd_gols)

infos_jogador['gols'] = gols
infos_jogador['total'] = total
print('-=' * 30)
print(infos_jogador) # Primeiro print da aula, exibe toda lista com chaves e valores.
print('-=' * 30)
for k, v in infos_jogador.items(): # Segundo print da aula, exibe chaves e seus respectivos valores
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {infos_jogador["nome"]} jogou {len(infos_jogador["gols"])} partidas.')

for qp in range(len(infos_jogador['gols'])): # terceiro print da aula, exibe o jogo e quantidade de gols em cada jogo
    print(f'\t=> Na partida {qp}, fez {infos_jogador["gols"][qp]} gols.')
print(f'Foi um total de {total} gols, um aproveitamento de {total / (len(infos_jogador["gols"]) ) * 100:.2f} %. \n') #Realiza um cálculo de aproveitamento (total de gols / quantidade de partidas) * 100
print('OBRIGADO E VOLTE SEMPRE :D\n')

# Resolução do curso
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['total'] = sum(partidas)
jogador['gols'] = partidas[:]
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
