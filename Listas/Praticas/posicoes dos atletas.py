'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 '''

posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
lista_geral = []

print('Obs: Para encerrar o programa não insira o nome do atleta.')

while True:
    tot = 0
    atleta = ""
    atleta = str(input('\nAtleta: ').capitalize())
    if not atleta:
        break
    lista_geral.append([atleta,[]])

    for s in range(5):
        saltos = float(input(f'{posicoes[s]} Salto: '))
        tot += saltos
        lista_geral[-1][1].append(saltos)

    media = tot / 5
    lista_geral[-1].append(media)

print('\nFinal: ')


