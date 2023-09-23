'''Escreva um programa que receba uma tupla de nomes e retorne uma nova tupla contendo apenas os nomes que começam com a letra 'A'.'''
nomes = ('Ana', 'Carlos', 'Vania', 'Herick', 'Alice', 'Abigail', 'Jose', 'Ferdinando')

for nome in nomes:
    procura = nome[0].lower().find('a') # a função find irá procurar a letra 'a' no primeiro indice dos elementos na tupla,os nome que tiverem irão retornar o valor 0, os que não tiverem vao retornar -1
    if procura == 0:
        print(nome.capitalize())

# Solução com o método startswitch() 
nomes = ('Ana', 'Carlos', 'Vania', 'Herick', 'Alice', 'Abigail', 'Jose', 'Ferdinando')

for nome in nomes:
    if nome.lower().startswith('a'):
        print(nome.capitalize())
