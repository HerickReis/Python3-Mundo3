# Parte do código
'''teste = list()
teste.append('Herick')
teste.append(18)
galera = list()
galera.append(teste[:])''' # Com o [:] a cópia será feita então os valores podem ser modificados individualmente em cada lista.

# teste
'''
galera.append(teste)
teste[0] = 'Maria' 
teste[1] = 22''' # Ao utilizar este método estamos realizando uma ligação da estrutura, assim toda mudança feita terá efeito nas duas listas.

#Parte do código
'''teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

# Outra forma de fazer listas composta
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

'print(galera[0])' # Exibir uma lista específica
'print(galera[0][1])' # exibir um item dentro de uma lista onde o primeira índice é a lista e o segundo o elemento.

'''for p in galera:
    print(p[1])''' # percorrer um item expessifico de cada lista.

'''for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

# Cria uma lista a cada loop e a adiciona em galera, logo após a lista dado é limpa.
'''galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:' )))
    galera.append(dado[:]) # Com o [:] cria uma cópia da lista dentro do append, sem o [:] apenas faz uma ligação entre elas onde cada mudança terá efeito em ambas.
    dado.clear()''' # Limpa a lista desejada, perfeito para criar dados temporários

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ' )))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')