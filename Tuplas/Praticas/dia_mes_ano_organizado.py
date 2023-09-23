'''Escreva um programa que receba uma tupla de datas no formato (dia, mês, ano) e ordene-as em ordem crescente.'''
datas = ((26, 6, 2023),(7, 8, 2006), (4,5,2024))

for data in sorted(datas):  
    dia = data[0]
    mes = data[1]
    ano = data[2]
    print(f'Dia: {dia:02} Mes: {mes:02} Ano: {ano}')