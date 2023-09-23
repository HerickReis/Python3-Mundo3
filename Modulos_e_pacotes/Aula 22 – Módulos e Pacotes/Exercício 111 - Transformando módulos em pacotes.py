'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''

from ex111.UtilidadesCev import moedas

valor = float(input('Valor: '))
aumento = float(input('Aumento de preço: '))
desconto = float(input('Desconto de preço: '))

moedas.resumo(valor,aumento,desconto)
