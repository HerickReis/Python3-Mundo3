'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

# Minha resolução (Parece que estou copiando das aulas ;-; )
'''def ficha(nome_jogador = '<Desconhecido>', gols_marcados = 0):
    """-- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    23/08/2023"""
    print(f'O jogador {nome_jogador} marcou {gols_marcados} gol(s) na partida.')


# Programa principal
jogador = str(input('Nome do jogador: ').strip().capitalize())
gols = str(input('Números de gols: ').strip())

if not jogador and not gols:
    ficha()

elif not jogador:
    ficha(gols_marcados=int(gols))

elif not gols or gols.isalpha():
    ficha(nome_jogador=jogador)

else:
    ficha(nome_jogador= jogador, gols_marcados=int(gols))'''




def ficha(jog= '<Desconhecido>',gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Resolução do curso
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
