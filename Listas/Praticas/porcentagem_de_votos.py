'''Desenvolver um programa em Python para realizar uma enquete entre os telespectadores de uma emissora de televisão.
As telefonistas utilizarão o programa para computar os votos dos jogadores, que são representados por números de 1 a 23.
O voto igual a zero indica o encerramento da votação.
Votos inválidos devem ser ignorados, exibindo uma breve mensagem de aviso.
Após o término da votação, o programa deve exibir o total de votos computados, os números dos jogadores que receberam votos, seus respectivos votos e percentuais de votos.
O programa deve utilizar arrays para armazenar os dados dos jogadores e dos votos.
Deve haver uma função para calcular o percentual de votos de cada jogador, recebendo como parâmetros o número de votos do jogador e o total de votos.
O resultado deve ser exibido ordenado pelo número do jogador.
O programa deve gravar os dados referentes ao resultado da votação em um arquivo texto no disco, com a mesma disposição apresentada na tela.

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''
total_votos = []
quantidade_de_votos = 0
while True:
    votos_jogadores = int(input('Número do jogador(Digite 0 para encerrar): '))
    if votos_jogadores == 0:
        break
    elif votos_jogadores not in range(1,24):
        print('Jogador inválido, Digite um número entre 1 e 23')
        continue

    quantidade_de_votos += 1
    verificar_jogador = False

    for jogador_em_lista in total_votos:
        if jogador_em_lista[0] == votos_jogadores:
            jogador_em_lista[1] += 1
            verificar_jogador = True
            break
    if not verificar_jogador:
        total_votos.append([votos_jogadores,1])

print(f'Foram computados {quantidade_de_votos} votos')
total_votos.sort()
print(total_votos)