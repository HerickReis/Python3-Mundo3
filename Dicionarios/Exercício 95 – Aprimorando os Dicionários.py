# Enunciado anterior
'''Crie um programa que gerencie o aproveitamento de um jogador da futebol.  O programa vai ler o nome do jogador quantas partidas ele jogou. 
Depois vai ler a quantidade de gols Feitos em cada partida partida.  
No Final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
# Agora
'''Aprimore o DESAFIO 093 para que ele Funcione com vários jogadores. 
incluindo um sistema de visualização de detalhas do aprovaitamento de cada jogador.'''
# Minha resolução
geral = []
while True:
    total = 0

    print('-' * 30)
    nome = str(input('Nome do jogador: ').capitalize().strip())
    qntd_partidas = int(input(f'Quantas partidas {nome} jogou? ').strip())
    geral.append({'nome': nome, 'partidas' : qntd_partidas, 'gols': []})

    for p in range(qntd_partidas):
        gols = int(input(f'Quantos gols na partida {p}: ').strip())
        total += gols
        geral[-1]['gols'].append(gols)

    geral[-1]['total'] = total

    r = str(input('Quer continuar? [S/N] ').strip()[0])
    while r not in 'SsNn':
        print('Informação inválida.')
        r = str(input('Quer continuar? [S/N] ').strip()[0])
    if r in 'Nn':
        break

espaço_fixo = 4
maximo_codigo = max(len(str(pos)) for pos in range(0, len(geral)))
maximo_nome = max(len(dados["nome"]) for dados in geral)
maximo_partidas = max(len(str(dados["partidas"])) for dados in geral)
maximo_gols = max(len(str(dados["gols"])) for dados in geral)
maximo_total = max(len(str(dados["total"])) for dados in geral)

print("Código" + " " * (maximo_codigo + espaço_fixo) + "Nome" + " " * (maximo_nome + espaço_fixo) + "Partidas" + " " * (maximo_partidas + espaço_fixo) + "Gols" + " " * (maximo_gols + espaço_fixo) + "Total" )

for codigo, dados in enumerate(geral) :
    nomes, partidas, gol, totais = dados["nome"], dados["partidas"], str(dados["gols"]), dados["total"]
    print(f"{codigo:<{maximo_codigo}}{' ' * (maximo_codigo + espaço_fixo + 5)}{nomes:<{maximo_nome}}{' ' * (espaço_fixo + 4)}{partidas:<{maximo_partidas}}{' ' * (espaço_fixo * 3)}{gol:<{maximo_gols}}{' ' * (espaço_fixo + 4)}{totais:<{maximo_total}}")

while True:
    busca = int(input('Mostrar dados de qual jogador(999 imterrompe)? '))
    if busca == 999:
        break

    elif busca not in range(0, len(geral)):
        print('Jogador inválido, tente novamente.')
        continue

    print(f'-- LEVANTAMENTO DO JOGADOR {geral[busca]["nome"]}')
    for p, g in enumerate(geral[busca]['gols']):
        print(f'Na partida {p + 1} fez {g} gols.')

# Resolução do curso
time = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostra dados de qual jogador? '))
    if busca == 999:
        break
    if busca>= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
