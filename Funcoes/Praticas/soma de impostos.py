'''Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def somaimposto(porcentagem_taxa, valor_item):
    valor_total = valor_item + (valor_item * porcentagem_taxa/100)
    print(f'{valor_total:.2f}')

# Programa principal
somaimposto(porcentagem_taxa=float(input('Porcentagem imposto: ')),valor_item=float(input('Valor do produto: ')))
