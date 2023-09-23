lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#              |           |       |       |
#              0           1       2       3
#              -4          -3      -2      -1 
#lanche[1] = 'Refrigerante' -- Tuplas são imutáveis
#print(lanche[1])

# sem posição
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caramba')

# mostrar posição do item
'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

# ordenar elementos
'''print(sorted(lanche))'''

'''a = (2, 5, 3)
b = (5, 8, 2, 1)
c = b + a
print(c) '''
# sorted irá ordenar a lista de forma alfabética.
# quando se utiliza o sinal de adição para tuplas elas nao irão somar os valores e sim irá juntar os valores
# saída (2, 5, 3, 5, 8, 2, 1)

'''print(c.index(5,1 ))'''

# irá mostar a posição do elemento entre parenteses
# se colocar o valor a ser procurado e outro valor após virgula, o numero apos a virgula será utilizdo como posicao minima, então ele irá procurar neste caso a partir da posica 1


# diferente de outras linguagens como Java o python aceita diferentes valores em suas variaveis compostas, em java se uma variavel composta possui strings(textos) ele irá aceitar apenas textos
#se tiver numeros irá aceitar apenas numerosç, mas o python aceita a diversificação sem problemas Ex:

pessoa = ('Herick', 18, 'M', 180)
print(pessoa)

#tuplas sao imutaveis ou seja nao podem ser modificadas, mas elas podem ser deletadas com a função del
del(pessoa)  #não só tuplas mas qualquer coisa pode ser deletada com esta função
