'''Crie uma tupla chamada meses com os nomes dos meses do ano. Imprima os meses em ordem inversa, usando um loop for.'''
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio','Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

for i in meses[::-1]:
    print(i)

'''for i in range(0, len(meses)):
    print(meses[i::-1])''' # fez uma especie de triangulo