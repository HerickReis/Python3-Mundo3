'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No Final, mostre uma listagem da preços, organizando os dados de Forma tabular.'''
print('\nMinha resolução\n'.upper())
produtos = (('Pao', 0.5), 
            ('Arroz', 18.0), 
            ('Laranja', 1.20), 
            ('Feijao', 6.48), 
            ('Refigerante', 3.56), 
            ('Queijo', 6.80), 
            ('Leite', 4.89), 
            ('Suco', 0.89), 
            ('Mortadela', 1.98),
            ('Presunto', 2.15))
print('-'*50)
print('Listagem de preços'.upper().center(45))
print('-'*50)
print('Produtos\t\t\tPreço')
print('_'*50)
for o in produtos:
    produtos,preco = o
    print(f'{produtos.ljust(33,".")}R$ {preco:.2f}')#o .ljust(x, '.') serve para adiconar simbolos a direita da string em que é colocado, neste cado ele irá adicionar pontos . a direita da variavel produtos
print('-'*50)

# Resolução do curso
print('\nResolução do curso\n'.upper())
listagem= (
'Pao', 0.5, 
'Arroz', 18.0, 
'Laranja', 1.20, 
'Feijao', 6.48, 
'Refigerante', 3.56, 
'Queijo', 6.80, 
'Leite', 4.89, 
'Suco', 0.89, 
'Mortadela', 1.98,
'Presunto', 2.15
)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
