'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 
1 – Janeiro, 2 – Fevereiro, . . . ).'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas_medias = []
temps = 0

for m in meses:
    temperatura_mensal = float(input(f'Digite a temperatura média de {m}: '))
    temperaturas_medias.append(temperatura_mensal)
    temps += temperatura_mensal

media_anual = int(temps / len(meses))

print(f'''A média anual é de {media_anual}°C 
Os meses com temperatura acima da média são: ''',end=' ')
for pos, mes in enumerate(meses):
    if temperaturas_medias[pos] > media_anual:
        if pos <= len(meses)-1:
            print(f'{pos+1} - {mes}',end=', ')
        else:
            print(f'{pos+1} - {mes}',end=' ')